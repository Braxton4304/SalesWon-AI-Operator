# Activity Prioritization

Defines how agents recommend **what to do next** and why.

## Priority Stack

1. **Revenue-critical** — Opportunities closing within window with missing actions
2. **SLA-critical** — Cases or commitments at risk
3. **Relationship** — Executive touchpoints, renewal checkpoints
4. **Hygiene** — CRM data quality, stale opportunities
5. **Prospecting** — New pipeline when capacity allows

## Inputs

- [ROI_SCORING_MODEL.md](ROI_SCORING_MODEL.md)
- [PIPELINE_HEALTH_MODEL.md](PIPELINE_HEALTH_MODEL.md)
- [SALES_PLAYBOOK.md](SALES_PLAYBOOK.md) chapter context
- User role and territory (Layer 4)

## Output Format

When recommending activities, include:

- Activity type
- Target record (opportunity/account/case ID)
- Rationale (grounded in CRM)
- Priority score
- Suggested due date

## TBD

- Rep capacity model (max recommendations per day)
- Manager override rules
