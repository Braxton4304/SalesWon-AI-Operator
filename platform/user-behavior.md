# User Behavior

RUNTIME_CONTEXT layer 6 — signals that personalize responses without overriding governance.

## Signals (Planned)

| Signal | Use |
|--------|-----|
| Preferred detail level | concise vs. verbose |
| Recent modules visited | CRM context priming |
| Role (rep, manager, CS) | Capability and visibility |
| Acceptance patterns | Prefer formats user keeps |
| Time of day / timezone | Scheduling recommendations |

## Collection

- Frontend events → Azure SQL or App Insights
- No PII in behavioral aggregates without policy

## Rules

- Behavior signals adjust tone and format — not permissions
- Cannot elevate write access based on behavior

## TBD

- Event schema
- Privacy opt-out (Layer 4 / compliance)
