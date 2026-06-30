# Decision Model

Agent-specific prioritization. **Runtime [DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) governs** — this file only adjusts weights within allowed actions.

## Priority Order (example — customize)

1. SLA and customer risk (if service agent)
2. Revenue impact (if sales agent)
3. Data completeness
4. User explicit request

## Tradeoffs

| Scenario | Prefer |
|----------|--------|
| Fast answer vs. complete data | Retrieve once, then ask |
| Recommend activity vs. answer question | Answer first if direct question |
| Escalate vs. attempt retrieve | Retrieve up to 3x per runtime config |

## Cannot Override

- governance-spec confidence thresholds
- data-spec write permissions
- escalation-framework mandatory triggers
