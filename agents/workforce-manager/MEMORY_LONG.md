# Long Memory

- Operator-preferred routing policies (e.g., always route account brief requests to account-research first)
- Historical conflict patterns by record type (aggregated, no customer PII)
- Workforce capacity threshold overrides per deployment (Layer 4)
- KPI alert thresholds customized by human leaders
- Escalation routing contact preferences (Layer 4 mapping)

## Org Memory

Per [shared/ORGANIZATIONAL_MEMORY.md](../../shared/ORGANIZATIONAL_MEMORY.md):

- Handoff matrix and division of labor (DIGITAL_WORKFORCE)
- Approval matrix summary for escalation routing context
- Corporate standards affecting cross-agent consistency checks

## Does Not Store

- Individual rep or CS agent user preferences (employee MEMORY_LONG scope)
- Raw CRM field values — query via audit sources only

```yaml
memory_long_version: "1.0.0"
scope: workforce_policy_preferences
pii_allowed: false
```
