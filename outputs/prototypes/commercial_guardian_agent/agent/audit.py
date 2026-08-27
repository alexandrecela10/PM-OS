"""Append-only, hash-chained audit log. Every kernel decision lands here."""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field


@dataclass(frozen=True)
class AuditEvent:
    seq: int
    ts: float
    actor: str
    action: str
    detail: dict
    prev_hash: str
    hash: str


@dataclass
class AuditLog:
    events: list[AuditEvent] = field(default_factory=list)

    def record(self, actor: str, action: str, detail: dict) -> AuditEvent:
        prev_hash = self.events[-1].hash if self.events else "genesis"
        seq = len(self.events)
        ts = time.time()
        payload = json.dumps(
            {"seq": seq, "actor": actor, "action": action, "detail": detail, "prev": prev_hash},
            sort_keys=True,
            default=str,
        )
        h = hashlib.sha256(payload.encode()).hexdigest()
        ev = AuditEvent(seq=seq, ts=ts, actor=actor, action=action, detail=detail, prev_hash=prev_hash, hash=h)
        self.events.append(ev)
        return ev

    def verify_chain(self) -> bool:
        prev = "genesis"
        for ev in self.events:
            payload = json.dumps(
                {"seq": ev.seq, "actor": ev.actor, "action": ev.action, "detail": ev.detail, "prev": prev},
                sort_keys=True,
                default=str,
            )
            if hashlib.sha256(payload.encode()).hexdigest() != ev.hash or ev.prev_hash != prev:
                return False
            prev = ev.hash
        return True

    def actions(self) -> list[str]:
        return [e.action for e in self.events]
