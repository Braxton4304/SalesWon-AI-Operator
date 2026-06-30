# Reference Agent

**Template agent** — copy this folder to create new agents.

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

## Spec Imports

| Spec | Path |
|------|------|
| Runtime | [specifications/runtime-spec.md](../../specifications/runtime-spec.md) → [runtime/](../../runtime/) |
| Governance | [specifications/governance-spec.md](../../specifications/governance-spec.md) |
| Data | [specifications/data-spec.md](../../specifications/data-spec.md) → [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md) |
| Agent | [specifications/agent-spec.md](../../specifications/agent-spec.md) |

## Shared Imports (example)

- [shared/SALES_PLAYBOOK.md](../../shared/SALES_PLAYBOOK.md)
- [shared/COMMUNICATION_STANDARD.md](../../shared/COMMUNICATION_STANDARD.md)

## File Index

| File | Status |
|------|--------|
| [IDENTITY.md](IDENTITY.md) | Template — replace |
| [MISSION.md](MISSION.md) | Template — replace |
| [CAPABILITIES.md](CAPABILITIES.md) | Template — replace |
| [LIMITATIONS.md](LIMITATIONS.md) | Template — replace |
| [BEHAVIOR.md](BEHAVIOR.md) | Template — replace |
| [DECISION_MODEL.md](DECISION_MODEL.md) | Template — replace |
| [TOOLS.md](TOOLS.md) | Template — replace |
| [MEMORY_SHORT.md](MEMORY_SHORT.md) | Template — replace |
| [MEMORY_LONG.md](MEMORY_LONG.md) | Template — replace |
| [PROMPTS.md](PROMPTS.md) | Template — replace |
| [OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md) | Template — extend per role |
| [QUALITY.md](QUALITY.md) | Template — replace |
| [METRICS.md](METRICS.md) | Template — replace |
| [ESCALATION.md](ESCALATION.md) | Template — replace |

## Runtime Import

This agent imports `runtime/` in full. Do not duplicate DECISION_ENGINE, GOVERNANCE, or RUNTIME_CONTEXT content here.
