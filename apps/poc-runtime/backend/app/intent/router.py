# implements: runtime-spec

"""Intent routing via LLM provider."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.intent.schemas import Intent
from app.llm.base import FieldExtraction, IntentClassification, LLMProvider


@dataclass
class RoutedIntent:
    classification: IntentClassification
    extraction: FieldExtraction


class IntentRouter:
    def __init__(self, llm: LLMProvider) -> None:
        self._llm = llm

    def route(
        self, message: str, history: list[dict[str, str]]
    ) -> RoutedIntent:
        classification = self._llm.classify_intent(message, history)
        extraction = self._llm.extract_fields(
            classification.intent, message, history
        )
        return RoutedIntent(classification=classification, extraction=extraction)

    @staticmethod
    def merge_fields(
        base: dict[str, Any], incoming: dict[str, Any]
    ) -> dict[str, Any]:
        merged = dict(base)
        merged.update({k: v for k, v in incoming.items() if v is not None})
        return merged
