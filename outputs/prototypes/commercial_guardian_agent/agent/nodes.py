"""Pipeline nodes. LLM only where judgment is needed; verification and
deadline math are deterministic code."""
from __future__ import annotations

import datetime as dt

from .llm import ExtractorAdapter
from .models import CandidateEvent, DeadlineResult, Document, Notice, NoticeStatus

# Notice periods per clause (days). Production: per-contract-form rules engine
# configured from the executed contract + amendment chain.
NOTICE_PERIODS = {"GC 4.12": 28, "GC 8.4": 28, "GC 13.1": 14}

# Clauses whose notice period was modified by an amendment. If the amendment
# document is missing from the archive, deadlines are PROVISIONAL.
AMENDED_CLAUSES = {"GC 13.1": "AMD-3"}


def extract_events(extractor: ExtractorAdapter, docs: list[Document]) -> list[CandidateEvent]:
    events: list[CandidateEvent] = []
    for doc in docs:
        events.extend(extractor.extract(doc))
    return events


def verify_citations(events: list[CandidateEvent], corpus: dict[str, Document]) -> list[CandidateEvent]:
    """Deterministic verifier: every citation must resolve to a real document
    and quote-match its text, or the event is downgraded (never surfaced)."""
    for event in events:
        ok = True
        verified = []
        for c in event.citations:
            doc = corpus.get(c.doc_id)
            if doc is not None and c.quote in doc.text:
                verified.append(type(c)(doc_id=c.doc_id, quote=c.quote, verified=True))
            else:
                verified.append(c)
                ok = False
        event.citations = verified
        if not ok:
            event.surfaced = False
            event.provisional = True
    return events


def compute_deadlines(events: list[CandidateEvent], docs_by_id: dict[str, Document], archive_doc_ids: set[str]) -> list[DeadlineResult]:
    results = []
    for event in events:
        if not event.surfaced:
            continue
        clause = event.clause_ref
        period = NOTICE_PERIODS.get(clause or "")
        if period is None:
            results.append(DeadlineResult(event.event_id, clause, None, None, True, "no notice period on record for clause"))
            continue
        trigger_doc = docs_by_id.get(event.citations[0].doc_id) if event.citations else None
        if trigger_doc is None:
            results.append(DeadlineResult(event.event_id, clause, None, None, True, "trigger document unavailable"))
            continue
        trigger = dt.date.fromisoformat(trigger_doc.date)
        deadline = trigger + dt.timedelta(days=period)
        amendment = AMENDED_CLAUSES.get(clause or "")
        if amendment and amendment not in archive_doc_ids:
            results.append(DeadlineResult(event.event_id, clause, trigger.isoformat(), deadline.isoformat(), True, f"amendment {amendment} referenced but missing from archive; deadline provisional"))
        else:
            results.append(DeadlineResult(event.event_id, clause, trigger.isoformat(), deadline.isoformat(), False, "computed from contract notice period"))
    return results


def draft_notice(event: CandidateEvent, deadline: DeadlineResult) -> Notice:
    provisional_flag = " [PROVISIONAL — verify before reliance]" if deadline.provisional else ""
    body = (
        f"NOTICE (DRAFT — requires named human approval before any use)\n"
        f"Re: {event.event_type.replace('_', ' ')} — clause {event.clause_ref}\n"
        f"Pursuant to clause {event.clause_ref}, we hereby give notice of the event evidenced in "
        f"{', '.join(c.doc_id for c in event.citations)}.\n"
        f"Notice deadline: {deadline.deadline_date}{provisional_flag}\n"
        f"Evidence: " + "; ".join(f'{c.doc_id}: "{c.quote}"' for c in event.citations)
    )
    return Notice(
        notice_id=f"ntc-{event.event_id}",
        event_id=event.event_id,
        body=body,
        assertions=list(event.citations),
        status=NoticeStatus.DRAFT,
    )
