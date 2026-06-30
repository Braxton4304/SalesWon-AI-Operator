---
spec_version: "1.0.0"
spec_id: agent-spec
title: SalesWon AI Agent Specification
---

# Agent Specification

Defines the required file structure, import contract, and output schema for every SalesWon AI agent.

## Scope

Each agent owns **domain expertise only**. Runtime, governance, and platform integration are imported — not redefined per agent.

## Required Files

Every agent folder MUST contain:

| File | Purpose |
|------|---------|
| `AGENT.md` | Index, runtime import contract, spec references |
| `IDENTITY.md` | Who am I? Role, audience, tone boundaries |
| `MISSION.md` | Why do I exist? Business outcome |
| `CAPABILITIES.md` | What am I allowed to do? |
| `LIMITATIONS.md` | What am I never allowed to do? |
| `BEHAVIOR.md` | Observable response patterns |
| `DECISION_MODEL.md` | Agent-specific prioritization (runtime DECISION_ENGINE governs) |
| `TOOLS.md` | Tool definitions and usage rules |
| `MEMORY_SHORT.md` | Current conversation and task scope |
| `MEMORY_LONG.md` | Preferences, history, org memory scope |
| `PROMPTS.md` | Prompt assembly fragments |
| `OUTPUT_SCHEMA.md` | Machine-readable response contract |
| `QUALITY.md` | Correctness, completeness, hallucination avoidance |
| `METRICS.md` | Acceptance rate, edits, escalation %, confidence, ROI |
| `ESCALATION.md` | When and how to escalate |

## Prohibited Files

- `SOUL.md` — replaced by operational enterprise files
- `MEMORY.md` — use SHORT + LONG split
- `EVALUATION.md` — use QUALITY + METRICS split

## Import Contract

```text
Agent Response =
  shared/ (industry IP)
  + runtime/ (orchestration, decision engine, governance)
  + platform/ (CRM data via data-spec)
  + agent/ (domain expertise)
  + customer config (Layer 4)
  + CRM context (Layer 5)
```

## OUTPUT_SCHEMA Requirements

Every agent MUST define a JSON schema in `OUTPUT_SCHEMA.md` including at minimum:

- `summary` — human-readable response summary
- `confidence` — float 0.0–1.0
- `sources` — array of grounding references (CRM record IDs, KB articles)
- `recommended_action` — optional; required when decision is `recommend`

Agent-specific fields are allowed (e.g. `customer_sentiment` for Customer Service).

## Machine-Readable Contract

```yaml
spec_version: "1.0.0"
spec_id: agent-spec
required_files:
  - AGENT.md
  - IDENTITY.md
  - MISSION.md
  - CAPABILITIES.md
  - LIMITATIONS.md
  - BEHAVIOR.md
  - DECISION_MODEL.md
  - TOOLS.md
  - MEMORY_SHORT.md
  - MEMORY_LONG.md
  - PROMPTS.md
  - OUTPUT_SCHEMA.md
  - QUALITY.md
  - METRICS.md
  - ESCALATION.md
prohibited_files:
  - SOUL.md
  - MEMORY.md
  - EVALUATION.md
output_schema_required_fields:
  - summary
  - confidence
  - sources
imports:
  - specifications/runtime-spec.md
  - specifications/governance-spec.md
  - specifications/data-spec.md
  - runtime/
  - shared/
template_path: agents/_template/
```

## References

- Implements: [runtime-spec.md](runtime-spec.md), [governance-spec.md](governance-spec.md), [data-spec.md](data-spec.md)
- Implemented by: [agents/](../agents/)
