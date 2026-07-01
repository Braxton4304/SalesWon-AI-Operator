# implements: agent-spec

"""Parse poc_agent_manifest.yaml."""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from app.config.settings import get_settings


@dataclass
class AgentManifestEntry:
    id: str
    files: list[str]
    domains: list[str] = field(default_factory=list)


@dataclass
class PocAgentManifest:
    display_name: str
    max_chars_per_file: int
    agents: list[AgentManifestEntry]
    shared: list[str]
    policies: list[str]

    def agent_ids(self) -> list[str]:
        return [a.id for a in self.agents]

    def get_agent(self, agent_id: str) -> AgentManifestEntry | None:
        for agent in self.agents:
            if agent.id == agent_id:
                return agent
        return None


@lru_cache
def load_manifest() -> PocAgentManifest:
    settings = get_settings()
    path = Path(settings.poc_agent_manifest_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parents[2] / settings.poc_agent_manifest_path
    with path.open("r", encoding="utf-8") as handle:
        raw: dict[str, Any] = yaml.safe_load(handle) or {}
    poc = raw.get("poc_assistant", raw)
    agents = [
        AgentManifestEntry(
            id=a["id"],
            files=a.get("files", []),
            domains=a.get("domains", []),
        )
        for a in poc.get("agents", [])
    ]
    return PocAgentManifest(
        display_name=poc.get("display_name", "SalesWon Assistant"),
        max_chars_per_file=poc.get("max_chars_per_file", 8000),
        agents=agents,
        shared=poc.get("shared", []),
        policies=poc.get("policies", []),
    )
