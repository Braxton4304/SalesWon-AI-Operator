# Approval Policy

## Workflow

```text
Agent Draft (recommend) → Human Review → ServiceNow Commit
```

## Approval Matrix (Defaults — Layer 4 overrides)

| Action | Approver |
|--------|----------|
| Customer email send | Record owner (rep/CS agent) |
| Case state change | CS agent or team lead |
| Opportunity stage to Commit+ | Sales manager |
| Discount/pricing | Sales manager / deal desk |
| Forecast category change | Sales manager |

Authority `request_approval` in AUTHORITY.md maps to this matrix.

```yaml
policy_id: approval
workflow: draft_human_commit
autonomous_execute_phase_1: false
```
