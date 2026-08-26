"""Model adapter boundary.

`ExtractorAdapter` is the interface a production model (open-weights,
self-hosted, in-region) plugs into. `DummyExtractor` is a deterministic
keyword-based stand-in so the eval harness runs offline, reproducibly, with
zero network and zero data egress. It is intentionally imperfect (misses some
signals, over-triggers on others) so detection evals measure something real.
"""
from __future__ import annotations

from typing import Protocol

from .models import CandidateEvent, Citation, Document

_RULES = [
    # (event_type, clause_ref, trigger phrases, confidence)
    ("differing_site_conditions", "GC 4.12", ("differing site conditions", "unforeseen ground", "unexpected subsurface"), 0.92),
    ("delay", "GC 8.4", ("delay to the critical path", "milestone will be late", "suspension of work"), 0.88),
    ("scope_change", "GC 13.1", ("instruction to add", "variation order", "additional scope"), 0.90),
    # Deliberately noisy rule: fires on routine language too (tests precision).
    ("delay", "GC 8.4", ("behind schedule",), 0.55),
    ("watch_item", None, ("possible resequencing", "may impact", "under review"), 0.35),
]

SURFACING_THRESHOLD = 0.6


class ExtractorAdapter(Protocol):
    def extract(self, doc: Document) -> list[CandidateEvent]: ...


class DummyExtractor:
    def extract(self, doc: Document) -> list[CandidateEvent]:
        events: list[CandidateEvent] = []
        if doc.doc_type == "contract":
            # Contracts define obligations; they don't report events.
            return events
        text = doc.text.lower()
        for event_type, clause, phrases, conf in _RULES:
            for phrase in phrases:
                if phrase in text:
                    idx = text.find(phrase)
                    quote = doc.text[idx : idx + len(phrase)]
                    events.append(
                        CandidateEvent(
                            event_id=f"evt-{doc.doc_id}-{event_type}",
                            project_id=doc.project_id,
                            event_type=event_type,
                            description=f"{event_type} signal in {doc.doc_id}: '{quote}'",
                            clause_ref=clause,
                            citations=[Citation(doc_id=doc.doc_id, quote=quote)],
                            confidence=conf,
                            surfaced=conf >= SURFACING_THRESHOLD,
                        )
                    )
                    break
        return events


class HallucinatingExtractor(DummyExtractor):
    """Adversarial adapter for evals: emits a citation to a document that does
    not exist. The deterministic verifier must catch and downgrade it."""

    def extract(self, doc: Document) -> list[CandidateEvent]:
        events = super().extract(doc)
        events.append(
            CandidateEvent(
                event_id=f"evt-{doc.doc_id}-fabricated",
                project_id=doc.project_id,
                event_type="delay",
                description="fabricated delay event with a citation that does not exist",
                clause_ref="GC 8.4",
                citations=[Citation(doc_id="LTR-9999", quote="the works are suspended indefinitely")],
                confidence=0.95,
                surfaced=True,
            )
        )
        return events
