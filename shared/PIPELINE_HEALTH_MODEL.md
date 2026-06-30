# Pipeline Health Model

Signals and scoring for sales pipeline health — manager visibility target.

## Health Signals

| Signal | Healthy | At Risk | Critical |
|--------|---------|---------|----------|
| Stage velocity | TBD | TBD | TBD |
| Close date slip | TBD | TBD | TBD |
| Activity recency | TBD | TBD | TBD |
| Amount / probability mismatch | TBD | TBD | TBD |
| Single-threaded deal | TBD | TBD | TBD |

## Aggregate Metrics

- Pipeline coverage ratio (pipeline / quota)
- Weighted pipeline value
- Stage conversion rates (historical baseline TBD)
- Forecast category distribution

## Agent Usage

- **Sales Manager Agent** — primary consumer
- **Sales Rep Agent** — individual deal health warnings

## Data Requirements

Per [data-spec](../specifications/data-spec.md): opportunity required fields must be present for high-confidence health scores.

## Machine-Readable Contract

```yaml
model_version: "1.0.0"
status: framework_only
primary_object: opportunity
signals: [stage_velocity, close_date_slip, activity_recency, amount_probability_gap, threading]
```
