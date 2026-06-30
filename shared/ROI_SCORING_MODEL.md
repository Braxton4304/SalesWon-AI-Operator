# ROI Scoring Model

Framework for ranking activities by expected return on sales effort.

## Inputs (from CRM)

- Opportunity amount and probability
- Activity type and recency
- Account tier / strategic value
- Pipeline stage velocity

## Scoring Dimensions (TBD)

| Dimension | Weight | Source |
|-----------|--------|--------|
| Revenue impact | TBD | opportunity |
| Time to close | TBD | opportunity.close_date |
| Win probability | TBD | opportunity.probability |
| Strategic account | TBD | account tier (Layer 4) |

## Output

- Priority score 0–100 for activity recommendations
- Used by [ACTIVITY_PRIORITIZATION.md](ACTIVITY_PRIORITIZATION.md) and runtime BUSINESS_REASONING

## Rules

- Scores MUST be computed from CRM data — never invented
- Missing fields → reduce confidence, do not guess amounts

## Machine-Readable Contract

```yaml
model_version: "1.0.0"
status: framework_only
requires_crm_fields: [amount, probability, close_date, stage]
```
