# implements: runtime-spec, runtime/MEMORY_MODEL.md

"""Short-term session memory."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4

from app.config.settings import load_runtime_config


@dataclass
class SessionState:
    session_id: str
    turns: list[dict[str, str]] = field(default_factory=list)
    pending_fields: dict[str, Any] = field(default_factory=dict)
    pending_intent: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ShortTermMemory:
    def __init__(self) -> None:
        config = load_runtime_config()
        short_cfg = config.get("memory", {}).get("short", {})
        self._max_turns = short_cfg.get("max_turns", 20)
        self._ttl_minutes = short_cfg.get("ttl_minutes", 120)
        self._sessions: dict[str, SessionState] = {}

    def get_or_create(self, session_id: str | None) -> SessionState:
        if session_id and session_id in self._sessions:
            session = self._sessions[session_id]
            if self._is_expired(session):
                del self._sessions[session_id]
            else:
                return session
        new_id = session_id or str(uuid4())
        session = SessionState(session_id=new_id)
        self._sessions[new_id] = session
        return session

    def _is_expired(self, session: SessionState) -> bool:
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=self._ttl_minutes)
        return session.updated_at < cutoff

    def add_turn(self, session: SessionState, role: str, content: str) -> None:
        session.turns.append({"role": role, "content": content})
        if len(session.turns) > self._max_turns:
            session.turns = session.turns[-self._max_turns :]
        session.updated_at = datetime.now(timezone.utc)

    def get_history(self, session: SessionState) -> list[dict[str, str]]:
        return list(session.turns)


_memory: ShortTermMemory | None = None


def get_short_term_memory() -> ShortTermMemory:
    global _memory
    if _memory is None:
        _memory = ShortTermMemory()
    return _memory
