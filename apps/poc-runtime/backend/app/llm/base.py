# implements: runtime-spec

"""Pluggable LLM provider interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.planning.results import PlanExecutionResult
    from app.planning.schema import ActionPlan
    from app.runtime.prompt_compiler import CompiledPrompt


class LLMNotConfigured(Exception):
    """Raised when Azure OpenAI credentials are not yet provisioned."""


class LLMProvider(ABC):
    @abstractmethod
    def plan(self, compiled: "CompiledPrompt") -> "ActionPlan":
        """Produce structured ActionPlan from compiled runtime prompt."""

    @abstractmethod
    def generate_response(
        self,
        plan: "ActionPlan",
        execution: "PlanExecutionResult",
        compiled: "CompiledPrompt",
    ) -> str:
        """Generate user-facing narrative after backend execution."""
