# Runtime

Implements: [specifications/runtime-spec.md](../specifications/runtime-spec.md), [specifications/governance-spec.md](../specifications/governance-spec.md)

The platform runtime is imported by every agent. Agents do not redefine runtime behavior.

## Files

| File | Purpose |
|------|---------|
| [CONFIG.yaml](CONFIG.yaml) | Model, thresholds, orchestration defaults |
| [INTERFACES.md](INTERFACES.md) | Machine-readable agent I/O contracts |
| [RUNTIME_CONTEXT.md](RUNTIME_CONTEXT.md) | Context assembly before every LLM call |
| [DECISION_ENGINE.md](DECISION_ENGINE.md) | Answer, ask, retrieve, escalate, refuse, recommend |
| [BUSINESS_REASONING.md](BUSINESS_REASONING.md) | Revenue, retention, velocity optimization |
| [GOVERNANCE.md](GOVERNANCE.md) | Audit, confidence, escalation enforcement |
| [SECURITY.md](SECURITY.md) | Auth, tenant isolation, secrets |
| [MEMORY_MODEL.md](MEMORY_MODEL.md) | Short vs. long memory tiers |

## Import Contract

```text
Every agent imports runtime/ — never copies or overrides without ADR.
```
