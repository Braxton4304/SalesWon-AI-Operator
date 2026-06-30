# Metrics

Operational and business metrics for this agent. Feeds platform observability and improvement loops.

## Operational Metrics

| Metric | Description | Target (Phase 1 pilot) |
|--------|-------------|--------------------------|
| Schema compliance rate | OUTPUT_SCHEMA validation pass % | ≥ 99% |
| Source grounding rate | Factual claims with ≥1 source_record | ≥ 98% |
| Hallucination incidents | Fabricated pipeline or forecast figures detected | 0 |
| Mean confidence | Average confidence score | ≥ 0.85 |
| Retrieval rate | % of turns using retrieve action | Track |
| Escalation rate | % of turns ending in escalate | < 10% |
| Ask/disambiguation rate | Ambiguous team/rep scope requests | Track |
| Tool sequence compliance | Standard pipeline review sequence followed | ≥ 95% |
| Priority score accuracy | Audit sample: DECISION_MODEL formula match | ≥ 90% |

## Quality Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Pipeline rollup accuracy | Totals match CRM team view on audit sample | ≥ 99% |
| Risk flag precision | forecast_risks align with PIPELINE_HEALTH_MODEL | ≥ 85% |
| Coaching evidence rate | rep_coaching_items with linked opp/activity IDs | 100% |
| Hygiene detection rate | data_hygiene_issues match PIPELINE_INSPECTION_GUIDE | ≥ 90% |
| Executive brief completeness | EXECUTIVE_SUMMARY_STANDARD sections when requested | 100% |
| Coverage ratio integrity | No invented quota denominators | 100% |

## Usage Metrics

| Metric | Description |
|--------|-------------|
| Brief acceptance rate | Manager uses output without major rewrite |
| Coaching item adoption | rep_coaching_items referenced in 1:1 (survey) |
| Manager action completion | manager_actions marked done by manager (Phase 2) |
| Repeat pipeline review | Same team reviewed within 7 days |
| Handoff citation rate | Follow-Up/Sales Rep references pipeline_summary (Phase 2) |
| Section skip rate | Manager requests subset (e.g., risks only) |

## Business KPIs

| KPI | Description | Link |
|-----|-------------|------|
| Forecast accuracy uplift | Manager-reported forecast variance reduction vs. prior quarter | SALES_PLAYBOOK ch. 10 |
| At-risk commit intervention rate | % of forecast_risks with documented manager action within 7 days | DECISION_MODEL |
| Pipeline coverage visibility | Managers with current coverage ratio from agent vs. manual rollup | PIPELINE_HEALTH_MODEL |
| Rep coaching effectiveness | Reps rate coaching items useful in 1:1 | PIPELINE_INSPECTION_GUIDE |
| Hygiene closure rate | data_hygiene_issues resolved in CRM within sprint window | ACTIVITY_PRIORITIZATION |
| Deal save rate | At-risk commit opps progressed or saved after intervention (Phase 2) | ROI_SCORING_MODEL |
| Exec brief time saved | Manager-reported minutes saved vs. manual prep | EXECUTIVE_SUMMARY_STANDARD |
| Forecast call preparedness | Manager confidence rating before forecast call (survey) | Pilot metric |

## Collection

Planned: `platform/observability.md` + Azure App Insights. Audit records per governance-spec.

```yaml
metrics_version: "1.0.0"
agent_id: sales-manager
primary_artifacts: [pipeline_summary, rep_coaching_items]
kpi_sections: [operational, quality, usage, business]
```
