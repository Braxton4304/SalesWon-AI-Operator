# implements: runtime-spec, runtime/DECISION_ENGINE.md

"""Clarification and confirmation pending-action store."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4


@dataclass
class PendingAction:
    pending_id: str
    session_id: str
    intent: str
    fields: dict[str, Any]
    proposed_action: dict[str, Any]
    actor: str
    tenant_id: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    ttl_minutes: int = 30


class ClarificationStore:
    def __init__(self) -> None:
        self._pending: dict[str, PendingAction] = {}

    def create(
        self,
        session_id: str,
        intent: str,
        fields: dict[str, Any],
        proposed_action: dict[str, Any],
        actor: str,
        tenant_id: str,
    ) -> PendingAction:
        pending = PendingAction(
            pending_id=str(uuid4()),
            session_id=session_id,
            intent=intent,
            fields=fields,
            proposed_action=proposed_action,
            actor=actor,
            tenant_id=tenant_id,
        )
        self._pending[pending.pending_id] = pending
        return pending

    def get(self, pending_id: str) -> PendingAction | None:
        action = self._pending.get(pending_id)
        if action and self._is_expired(action):
            del self._pending[pending_id]
            return None
        return action

    def pop(self, pending_id: str) -> PendingAction | None:
        action = self.get(pending_id)
        if action:
            del self._pending[pending_id]
        return action

    def _is_expired(self, action: PendingAction) -> bool:
        cutoff = action.created_at + timedelta(minutes=action.ttl_minutes)
        return datetime.now(timezone.utc) > cutoff


_store: ClarificationStore | None = None


def get_clarification_store() -> ClarificationStore:
    global _store
    if _store is None:
        _store = ClarificationStore()
    return _store
