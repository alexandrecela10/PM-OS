"""Governance kernel: policy checked BEFORE any node executes.

There is intentionally no "send" capability anywhere in this module or the
agent. The kernel enforces scope, an action allowlist, data residency, and a
named-human approval gate, and audits every decision.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .audit import AuditLog
from .models import Document, Notice, NoticeStatus, Residency

ALLOWED_ACTIONS = frozenset(
    {"ingest", "extract", "link_evidence", "verify_citations", "compute_deadlines", "draft_notice", "queue_for_approval", "register_event", "answer_question"}
)

STRATEGY_MARKERS = ("should we file", "should we claim", "recommend a claim", "legal strategy", "what is our entitlement strategy")


class GovernanceRefusal(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


@dataclass
class Policy:
    project_id: str
    agent_owner: str  # accountable owner in customer org (e.g. PMO head)
    approvers: frozenset[str]  # named humans allowed to approve notices
    residency: Residency = Residency.IN_REGION


@dataclass
class GovernanceKernel:
    policy: Policy
    audit: AuditLog = field(default_factory=AuditLog)

    def authorize(self, actor: str, action: str, detail: dict | None = None) -> None:
        detail = detail or {}
        if action not in ALLOWED_ACTIONS:
            self.audit.record(actor, "refusal.capability", {"action": action, **detail})
            raise GovernanceRefusal("capability", f"action '{action}' is not in the agent's allowlist")
        self.audit.record(actor, f"authorized.{action}", detail)

    def admit_document(self, actor: str, doc: Document) -> bool:
        """Scope + residency gate at ingest. Out-of-scope docs are refused,
        logged, and escalated to the agent owner — never silently processed."""
        if doc.project_id != self.policy.project_id:
            self.audit.record(actor, "refusal.out_of_scope", {"doc_id": doc.doc_id, "doc_project": doc.project_id, "escalated_to": self.policy.agent_owner})
            return False
        if doc.residency != self.policy.residency:
            self.audit.record(actor, "refusal.residency", {"doc_id": doc.doc_id, "residency": doc.residency, "escalated_to": self.policy.agent_owner})
            return False
        self.audit.record(actor, "admitted.document", {"doc_id": doc.doc_id})
        return True

    def check_question(self, actor: str, question: str) -> str | None:
        """Overreach boundary: legal strategy questions are refused with routing."""
        q = question.lower()
        if any(m in q for m in STRATEGY_MARKERS):
            self.audit.record(actor, "refusal.overreach", {"question": question, "routing": "counsel_review"})
            return ("I can provide the factual record, the contract's entitlement mechanics, and the "
                    "notice deadline. Claim strategy is a decision for your commercial team and counsel.")
        return None

    def approve_notice(self, approver: str, notice: Notice) -> Notice:
        """The only path from PENDING_APPROVAL to APPROVED. Named humans only."""
        if approver not in self.policy.approvers:
            self.audit.record(approver, "refusal.approval_unauthorized", {"notice_id": notice.notice_id})
            raise GovernanceRefusal("approval", f"'{approver}' is not a registered approver")
        if notice.status != NoticeStatus.PENDING_APPROVAL:
            self.audit.record(approver, "refusal.approval_bad_state", {"notice_id": notice.notice_id, "status": notice.status})
            raise GovernanceRefusal("approval", f"notice {notice.notice_id} is not pending approval")
        if any(not c.verified for c in notice.assertions):
            self.audit.record(approver, "refusal.approval_unverified_assertions", {"notice_id": notice.notice_id})
            raise GovernanceRefusal("approval", "notice contains unverified assertions")
        notice.status = NoticeStatus.APPROVED
        notice.approved_by = approver
        self.audit.record(approver, "approved.notice", {"notice_id": notice.notice_id})
        return notice
