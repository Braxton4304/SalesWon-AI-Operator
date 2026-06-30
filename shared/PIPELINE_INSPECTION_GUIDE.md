# Pipeline Inspection Guide

Used by: Sales Manager. Implements PIPELINE_HEALTH_MODEL.

## Inspection Checklist

- [ ] Required opp fields complete (amount, probability, close_date, owner)
- [ ] Stage age vs benchmark
- [ ] Activity recency < 14 days on commit deals
- [ ] Probability aligned to stage
- [ ] Forecast category justified
- [ ] Multi-threading (2+ contacts on late stage)

## Coaching Output

Rep-specific, constructive language per BEHAVIOR.md.

```yaml
playbook_id: pipeline_inspection
primary_agent: sales-manager
```
