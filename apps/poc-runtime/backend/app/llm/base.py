# implements: runtime-spec

"""Pluggable LLM provider interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from app.intent.schemas import Intent


@dataclass
class IntentClassification:
    intent: Intent
    confidence: float
    raw_text: str = ""


@dataclass
class FieldExtraction:
    fields: dict[str, Any] = field(default_factory=dict)
    missing_required: list[str] = field(default_factory=list)
    confidence: float = 0.0


class LLMNotConfigured(Exception):
    """Raised when Azure OpenAI credentials are not yet provisioned."""


class LLMProvider(ABC):
    @abstractmethod
    def classify_intent(self, message: str, history: list[dict[str, str]]) -> IntentClassification:
        ...

    @abstractmethod
    def extract_fields(
        self, intent: Intent, message: str, history: list[dict[str, str]]
    ) -> FieldExtraction:
        ...

    @abstractmethod
    def generate_response(
        self,
        intent: Intent,
        decision_action: str,
        context: dict[str, Any],
    ) -> str:
        ...
