# Escalation Framework

Implements: [specifications/governance-spec.md](../specifications/governance-spec.md)

## Triggers

| Trigger | Default Action |
|---------|----------------|
| Confidence below threshold | Escalate to human |
| Write permission denied | Refuse or recommend with human approval |
| User requests human | Escalate immediately |
| Policy violation detected | Refuse + escalate to admin |
| Retrieval failure (≥ 3 attempts) | Escalate with context |
| Legal / hostile communication | Escalate to designated contact |
| Sensitive data classification | Escalate per Layer 4 rules |

## Escalation Payload

Must include:

- Original user request
- Agent summary of attempted actions
- Confidence score and blocking reason
- Source references gathered
- Suggested assignee role (from Layer 4 contacts)

## Routing (Layer 4)

- Escalation contacts defined per customer deployment
- ServiceNow assignment group mapping TBD

## Agent Files

Each agent defines role-specific escalation in `ESCALATION.md`.

## Cross-References

- [runtime/DECISION_ENGINE.md](../runtime/DECISION_ENGINE.md)
- [CUSTOMER_SERVICE_FRAMEWORK.md](CUSTOMER_SERVICE_FRAMEWORK.md)
