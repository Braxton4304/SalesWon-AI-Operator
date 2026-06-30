# implements: runtime-spec, governance-spec

"""Application settings loaded from environment and runtime CONFIG.yaml."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: str = "local"
    tenant_id: str = "dev-tenant"
    llm_provider: str = "rule_based"
    connector: str = "servicenow"
    audit_log_path: str = "./audit/events.jsonl"
    runtime_config_path: str = "../../../runtime/CONFIG.yaml"

    azure_openai_endpoint: str = ""
    azure_openai_api_key: str = ""
    azure_openai_deployment: str = ""

    servicenow_instance_url: str = ""
    servicenow_client_id: str = ""
    servicenow_client_secret: str = ""
    servicenow_username: str = ""
    servicenow_password_or_token: str = ""

    @property
    def azure_openai_configured(self) -> bool:
        return bool(
            self.azure_openai_endpoint
            and self.azure_openai_api_key
            and self.azure_openai_deployment
        )

    @property
    def servicenow_configured(self) -> bool:
        return bool(
            self.servicenow_instance_url
            and self.servicenow_client_id
            and self.servicenow_client_secret
            and (self.servicenow_username or self.servicenow_password_or_token)
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


def load_runtime_config(settings: Settings | None = None) -> dict[str, Any]:
    settings = settings or get_settings()
    config_path = Path(settings.runtime_config_path)
    if not config_path.is_absolute():
        config_path = Path(__file__).resolve().parents[2] / settings.runtime_config_path
    if not config_path.exists():
        return {
            "governance": {
                "confidence_thresholds": {"high": 0.85, "medium": 0.60, "low": 0.59},
            },
            "decision_engine": {
                "default_action_on_ambiguity": "ask",
                "max_retrieval_attempts": 3,
            },
            "memory": {"short": {"max_turns": 20, "ttl_minutes": 120}},
        }
    with config_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}
