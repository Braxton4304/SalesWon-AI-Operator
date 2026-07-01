# implements: agent-spec

"""Load Digital Employee markdown contracts from repo agents/."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from app.agent.manifest import AgentManifestEntry, PocAgentManifest, load_manifest
from app.config.settings import get_settings


def _repo_root() -> Path:
    settings = get_settings()
    root = Path(settings.agent_repo_root)
    if not root.is_absolute():
        root = Path(__file__).resolve().parents[2] / settings.agent_repo_root
    return root.resolve()


def _read_file(rel_path: str, max_chars: int) -> str:
    path = _repo_root() / rel_path
    if not path.exists():
        return f"[missing: {rel_path}]"
    content = path.read_text(encoding="utf-8")
    if len(content) > max_chars:
        return content[:max_chars] + "\n\n[truncated for POC context limit]"
    return content


def load_agent_files(agent: AgentManifestEntry, manifest: PocAgentManifest) -> dict[str, str]:
    root = _repo_root()
    loaded: dict[str, str] = {}
    for filename in agent.files:
        rel = f"agents/{agent.id}/{filename}"
        loaded[filename] = _read_file(rel, manifest.max_chars_per_file)
    return loaded


def load_shared_and_policies(manifest: PocAgentManifest) -> dict[str, str]:
    loaded: dict[str, str] = {}
    for rel in manifest.shared + manifest.policies:
        loaded[rel] = _read_file(rel, manifest.max_chars_per_file)
    return loaded


def compile_agent_context(primary_agent_id: str) -> str:
    manifest = load_manifest()
    sections: list[str] = []

    agent = manifest.get_agent(primary_agent_id) or manifest.agents[0]
    sections.append(f"## Primary agent: {agent.id}")
    for filename, content in load_agent_files(agent, manifest).items():
        sections.append(f"### {agent.id}/{filename}\n{content}")

    sections.append("## Cross-agent limitations (union)")
    for other in manifest.agents:
        if other.id == agent.id:
            continue
        lim = _read_file(f"agents/{other.id}/LIMITATIONS.md", 2000)
        if lim and not lim.startswith("[missing"):
            sections.append(f"### {other.id} LIMITATIONS\n{lim}")

    sections.append("## Shared runtime + policies")
    for rel, content in load_shared_and_policies(manifest).items():
        sections.append(f"### {rel}\n{content}")

    return "\n\n".join(sections)


@lru_cache
def load_all_agent_ids() -> tuple[str, ...]:
    return tuple(load_manifest().agent_ids())
