# implements: runtime-spec, runtime/RUNTIME_CONTEXT.md

"""Context assembly — delegates to PromptCompiler for unscripted agent runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.memory.short_term import SessionState
from app.runtime.prompt_compiler import CompiledPrompt, PromptCompiler
from app.security.user_context import CurrentUserContext

# Re-export CompiledPrompt as RuntimeContext alias for backward compatibility
RuntimeContext = CompiledPrompt


def assemble_context(
    user_ctx: CurrentUserContext,
    message: str,
    history: list[dict[str, str]],
    crm_context: dict[str, Any] | None = None,
    extra: dict[str, Any] | None = None,
) -> CompiledPrompt:
    session = SessionState(session_id="legacy")
    session.turns = list(history)
    compiler = PromptCompiler()
    return compiler.compile(user_ctx, session, message, extra)
