"""Explicit DAG pipeline. Independent per-document extraction fans out in
parallel; the governance chain (verify -> deadlines -> draft -> approve) is
strictly sequential by design."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

from .governance import GovernanceKernel
from .llm import ExtractorAdapter
from .models import CandidateEvent, DeadlineResult, Document, Notice, NoticeStatus
from .nodes import compute_deadlines, draft_notice, verify_citations

AGENT_ACTOR = "commercial-guardian-agent"


@dataclass
class PipelineResult:
    admitted_docs: list[Document] = field(default_factory=list)
    refused_docs: list[Document] = field(default_factory=list)
    events: list[CandidateEvent] = field(default_factory=list)
    deadlines: list[DeadlineResult] = field(default_factory=list)
    notices: list[Notice] = field(default_factory=list)


class CommercialGuardianPipeline:
    def __init__(self, kernel: GovernanceKernel, extractor: ExtractorAdapter, max_workers: int = 4):
        self.kernel = kernel
        self.extractor = extractor
        self.max_workers = max_workers

    def run(self, documents: list[Document]) -> PipelineResult:
        result = PipelineResult()

        # 1. Policy gate at ingest (pre-execution, per document).
        self.kernel.authorize(AGENT_ACTOR, "ingest", {"n_docs": len(documents)})
        for doc in documents:
            (result.admitted_docs if self.kernel.admit_document(AGENT_ACTOR, doc) else result.refused_docs).append(doc)

        corpus = {d.doc_id: d for d in result.admitted_docs}

        # 2. Parallel fan-out: per-document extraction is independent work.
        self.kernel.authorize(AGENT_ACTOR, "extract", {"n_docs": len(result.admitted_docs)})
        with ThreadPoolExecutor(max_workers=self.max_workers) as pool:
            for doc_events in pool.map(self.extractor.extract, result.admitted_docs):
                result.events.extend(doc_events)

        # 3. Deterministic citation verification (structural hallucination catch).
        self.kernel.authorize(AGENT_ACTOR, "verify_citations", {"n_events": len(result.events)})
        result.events = verify_citations(result.events, corpus)

        # 4. Deterministic deadline rules engine.
        self.kernel.authorize(AGENT_ACTOR, "compute_deadlines")
        result.deadlines = compute_deadlines(result.events, corpus, set(corpus))

        # 5. Draft notices; queue for named-human approval. The pipeline ends
        #    at PENDING_APPROVAL — there is no send capability.
        deadlines_by_event = {d.event_id: d for d in result.deadlines}
        for event in result.events:
            if not event.surfaced or event.event_id not in deadlines_by_event:
                continue
            self.kernel.authorize(AGENT_ACTOR, "draft_notice", {"event_id": event.event_id})
            notice = draft_notice(event, deadlines_by_event[event.event_id])
            self.kernel.authorize(AGENT_ACTOR, "queue_for_approval", {"notice_id": notice.notice_id})
            notice.status = NoticeStatus.PENDING_APPROVAL
            result.notices.append(notice)

        return result

    def answer(self, question: str) -> str:
        refusal = self.kernel.check_question(AGENT_ACTOR, question)
        if refusal is not None:
            return refusal
        self.kernel.authorize(AGENT_ACTOR, "answer_question", {"question": question})
        return "Factual record response (v1 stub): see event register and evidence chains."
