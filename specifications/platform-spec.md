---
spec_version: "1.0.0"
spec_id: platform-spec
title: SalesWon AI Platform Specification
---

# Platform Specification

Defines the layered architecture, folder boundaries, and extension rules for the SalesWon AI operating system.

## Scope

This spec governs:

- Five operational layers plus a specifications layer
- Folder layout and naming conventions
- What belongs in repo vs. customer deployment vs. live CRM data
- Extension rules for new domains, agents, and products

## Layer Model

```text
Layer 0: /specifications     — Contracts (this folder)
Layer 1: /shared             — Business standards (reusable industry IP)
Layer 2: /runtime            — Platform runtime (orchestration, governance)
Layer 3: /agents             — Agent role specifications
Layer 4: Customer config     — Per-deployment (NOT in this repo, Phase 1)
Layer 5: Customer data       — Live CRM (NEVER in source control)
```

Integration surfaces live in `/platform` and implement [data-spec.md](data-spec.md) and platform boundaries defined here.

Blueprint and design exploration live in `/architecture` (SalesWon AI Platform workspace).

## Governed Response Pipeline

```text
Business Standards → Runtime → Agent → Customer Config → CRM Context → LLM → Governed Response
```

## Extension Rules

1. **New agent** — Copy `agents/_template/`; fill domain files; do not modify runtime without ADR in `architecture/DECISIONS.md`.
2. **New business domain** — Add top-level folder (e.g. `/commercial/`) with README charter only; no empty placeholder trees.
3. **New product** — Import `/specifications` as submodule or package; implement customer layers only.
4. **New CRM object** — Update `data-spec.md` first, then `platform/DATA_DICTIONARY.md`.

## Machine-Readable Contract

```yaml
spec_version: "1.0.0"
spec_id: platform-spec
layers:
  - id: specifications
    path: /specifications
    mutable_by: platform_team
  - id: business_standards
    path: /shared
    implements: [platform-spec, governance-spec]
  - id: runtime
    path: /runtime
    implements: [runtime-spec, governance-spec]
  - id: agents
    path: /agents
    implements: [agent-spec, runtime-spec]
  - id: platform_integrations
    path: /platform
    implements: [platform-spec, data-spec]
  - id: customer_configuration
    path: /deployments/{customer}/config
    in_repo: false
  - id: customer_data
    path: external_crm
    in_repo: false
extension:
  new_agent: copy_from agents/_template
  new_domain: top_level_readme_only
  spec_change_requires: architecture/DECISIONS.md entry
```

## References

- Implements: none (root contract)
- Implemented by: `README.md`, `architecture/`, `platform/`, folder layout
