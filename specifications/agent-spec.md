---
spec_version: "1.1.0"
spec_id: agent-spec
title: SalesWon AI Digital Employee Specification
---

# Agent Specification

Defines the required file structure for every **Digital Employee** and the Workforce Manager spec.

## Scope

Each agent owns domain expertise only. Runtime, governance, policies, and platform are imported.

## Required Files (22)

| File | Answers |
|------|---------|
| `AGENT.md` | Index and imports |
| `IDENTITY.md` | Who am I? |
| `MISSION.md` | Why do I exist? |
| `CAPABILITIES.md` | What can I do? |
| `LIMITATIONS.md` | Hard prohibitions |
| `BEHAVIOR.md` | Response patterns |
| `DECISION_MODEL.md` | Weighted priority formula |
| `TOOLS.md` | ServiceNow tools |
| `MEMORY_SHORT.md` | Session memory |
| `MEMORY_LONG.md` | User-scoped long memory |
| `PROMPTS.md` | Prompt fragments |
| `OUTPUT_SCHEMA.md` | Input→Audit pipeline + JSON |
| `QUALITY.md` | Quality bar + demo scenarios |
| `METRICS.md` | Operational + Business KPIs |
| `ESCALATION.md` | Pre-defined triggers |
| `AUTHORITY.md` | Can I do this? |
| `ACCOUNTABILITY.md` | Am I succeeding? |
| `COLLABORATION.md` | Handoffs and produces/consumes |
| `REASONING_PATTERNS.md` | Reasoning chain |
| `TRUST_MODEL.md` | Why trust this? |
| `EXPLAINABILITY.md` | Why this recommendation? |
| `BUSINESS_OBJECTIVES.md` | Outcome drivers |

## Prohibited Files

SOUL.md, MEMORY.md, EVALUATION.md

## Import Contract

```text
policies/ + shared/ + runtime/ + platform/ + agent/ + Layer 4 + CRM
```

## Machine-Readable Contract

```yaml
spec_version: "1.1.0"
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
  - AUTHORITY.md
  - ACCOUNTABILITY.md
  - COLLABORATION.md
  - REASONING_PATTERNS.md
  - TRUST_MODEL.md
  - EXPLAINABILITY.md
  - BUSINESS_OBJECTIVES.md
imports:
  - specifications/accountability-spec.md
  - specifications/workforce-spec.md
  - specifications/runtime-spec.md
  - specifications/governance-spec.md
  - specifications/data-spec.md
  - policies/
  - runtime/
  - shared/
template_path: agents/_template/
file_count: 22
```

## References

- Implements: runtime-spec, governance-spec, data-spec, workforce-spec, accountability-spec
- Implemented by: [agents/](../agents/)
