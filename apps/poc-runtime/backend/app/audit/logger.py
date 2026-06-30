# implements: governance-spec

"""JSONL audit logger."""

from __future__ import annotations

from pathlib import Path
from threading import Lock

from app.audit.schema import AuditRecord
from app.config.settings import get_settings


class AuditLogger:
    def __init__(self, log_path: str | None = None) -> None:
        settings = get_settings()
        self._log_path = Path(log_path or settings.audit_log_path)
        self._lock = Lock()
        self._log_path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, record: AuditRecord) -> AuditRecord:
        with self._lock:
            with self._log_path.open("a", encoding="utf-8") as handle:
                handle.write(record.to_jsonl() + "\n")
        return record


_audit_logger: AuditLogger | None = None


def get_audit_logger() -> AuditLogger:
    global _audit_logger
    if _audit_logger is None:
        _audit_logger = AuditLogger()
    return _audit_logger
