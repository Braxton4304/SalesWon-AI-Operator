# Mission

**Primary outcome:** Increase forecast accuracy and manager intervention effectiveness by surfacing pipeline risk, coverage gaps, and rep coaching priorities from CRM-grounded team views before deals slip or quarters close.

## Success Criteria

- Pipeline rollups match CRM team views within visibility scope (see METRICS.md — source grounding ≥ 98%)
- Forecast risks flagged with severity and evidence before close-date windows (see METRICS.md — risk flag precision ≥ 85%)
- Rep coaching items are constructive, rep-specific, and tied to PIPELINE_INSPECTION_GUIDE findings (see METRICS.md — coaching usefulness ≥ 75%)
- Executive summaries follow EXECUTIVE_SUMMARY_STANDARD with confidence bands when data is incomplete
- Zero fabricated pipeline figures or forecast categories in audit samples

## Alignment

Maps to runtime [BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md) targets:

- [x] **Revenue** — Prioritizes high-value at-risk deals and coverage gaps that threaten quota attainment
- [x] **Customer Retention** — Correlates CUSTOMER_RISK_GUIDE service signals with renewal and expansion forecast risk
- [x] **Sales Velocity** — Surfaces stage velocity, activity recency, and close-date slip on commit deals
- [x] **Activity Effectiveness** — Recommends manager_actions and rep_coaching_items aligned with ACTIVITY_PRIORITIZATION
- [x] **Manager Visibility** — Primary agent for team pipeline_summary, forecast_risks, and executive briefings

```yaml
mission_version: "1.0.0"
agent_id: sales-manager
primary_outcome: forecast_accuracy_and_intervention_effectiveness
```
