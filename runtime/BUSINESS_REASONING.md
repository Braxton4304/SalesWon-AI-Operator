# Business Reasoning

Implements: [specifications/runtime-spec.md](../specifications/runtime-spec.md)

The AI optimizes for **business outcomes**, not merely answering questions.

## Optimization Targets

| Target | Description | Signals |
|--------|-------------|---------|
| **Revenue** | Pipeline progression, deal velocity, expansion | Opportunity stage, amount, close date |
| **Customer Retention** | Risk detection, renewal health, case resolution | Case SLA, sentiment, activity gaps |
| **Sales Velocity** | Reduce idle time, prioritize high-impact activities | Activity prioritization model |
| **Activity Effectiveness** | Right action, right account, right time | ROI scoring, playbook stage |
| **Manager Visibility** | Forecast accuracy, pipeline health, team coverage | Pipeline health model, exec summary |

## Reasoning Integration

Business reasoning influences:

1. **Decision engine** — prefer `recommend` actions that advance pipeline vs. informational `answer`
2. **Activity prioritization** — rank suggestions using [shared/ACTIVITY_PRIORITIZATION.md](../shared/ACTIVITY_PRIORITIZATION.md)
3. **Confidence weighting** — revenue-impacting assertions require higher confidence (TBD per customer Layer 4)
4. **Escalation** — customer risk signals may lower escalation threshold

## Not In Scope

- Pricing or contract terms (unless direct arch impact)
- Fabricated ROI numbers without CRM grounding

## Machine-Readable Contract

```yaml
implements: runtime-spec
optimization_targets:
  - id: revenue
    weight: 1.0
    signals: [opportunity_stage, amount, close_date]
  - id: customer_retention
    weight: 1.0
    signals: [case_sla, sentiment, activity_gaps]
  - id: sales_velocity
    weight: 0.9
    signals: [activity_prioritization]
  - id: activity_effectiveness
    weight: 0.9
    signals: [roi_scoring, playbook_stage]
  - id: manager_visibility
    weight: 0.8
    signals: [pipeline_health, forecast_accuracy]
shared_imports:
  - shared/SALES_PLAYBOOK.md
  - shared/ACTIVITY_PRIORITIZATION.md
  - shared/PIPELINE_HEALTH_MODEL.md
  - shared/ROI_SCORING_MODEL.md
```

## Response Formula

```text
Sales Knowledge (shared/) + ServiceNow Data + User Behavior + Runtime = Governed Response
```
