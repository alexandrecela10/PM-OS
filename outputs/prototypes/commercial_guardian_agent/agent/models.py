"""Core datatypes for the Commercial Guardian agent."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Residency(str, Enum):
    IN_REGION = "in-region"
    OUT_OF_REGION = "out-of-region"


class NoticeStatus(str, Enum):
    DRAFT = "DRAFT"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    APPROVED = "APPROVED"
    REGISTERED = "REGISTERED"


@dataclass(frozen=True)
class Document:
    doc_id: str
    project_id: str
    doc_type: str  # letter | minutes | schedule_update | contract | daily_report
    date: str
    text: str
    residency: Residency = Residency.IN_REGION


@dataclass(frozen=True)
class Citation:
    doc_id: str
    quote: str
    verified: bool = False


@dataclass
class CandidateEvent:
    event_id: str
    project_id: str
    event_type: str  # differing_site_conditions | delay | scope_change | contradiction | watch_item
    description: str
    clause_ref: Optional[str]
    citations: list[Citation] = field(default_factory=list)
    confidence: float = 0.0
    surfaced: bool = False
    provisional: bool = False


@dataclass
class DeadlineResult:
    event_id: str
    clause_ref: Optional[str]
    trigger_date: Optional[str]
    deadline_date: Optional[str]
    provisional: bool
    reason: str


@dataclass
class Notice:
    notice_id: str
    event_id: str
    body: str
    assertions: list[Citation]
    status: NoticeStatus = NoticeStatus.DRAFT
    approved_by: Optional[str] = None
