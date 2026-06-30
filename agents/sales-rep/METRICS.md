# Metrics

Implements: [ACCOUNTABILITY.md](ACCOUNTABILITY.md), [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md)

## Operational KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Schema compliance rate | ≥ 99% | OUTPUT_SCHEMA validation pass % |
| Opp fact accuracy | ≥ 95% | Audit sample vs. CRM source_records |
| Source grounding rate | ≥ 98% | Factual claims with source_records citation |
| Mean confidence (answered) | ≥ 0.85 | TRUST_MODEL band distribution |
| Priority score formula compliance | ≥ 90% | Audit sample: DECISION_MODEL match |
| Escalation rate (pricing) | Track | escalation_required=true on discount requests |
| Missing_data disclosure rate | 100% | When required fields absent |

## Quality KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Next-best-action acceptance | ≥ 65% | Rep accepts or completes recommended action |
| Qualification gap usefulness | ≥ 80% | Rep survey on MEDDIC/SPIN/Sandler gaps |
| Email/activity draft acceptance | ≥ 60% | suggested_follow_up sent or edited-usefully |
| recommended_questions usage | Track | Questions used in logged activities (Phase 2) |
| Explainability satisfaction | ≥ 75% | "Why" response survey (pilot) |
| Zero hallucination incidents | 0 | Audit: fabricated CRM values |

## Usage KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Deal review response latency | < 8s P95 | End-to-end with CRM retrieve |
| Pipeline today ranking accuracy | ≥ 90% | Top opp matches DECISION_MODEL on audit |
| Retrieve cycles before answer | ≤ 2 avg | Tool chain efficiency |
| escalation_required precision | ≥ 95% | Escalations match ESCALATION.md triggers |

## Business KPIs

| Metric | Target | Driver |
|--------|--------|--------|
| Pipeline velocity | Track (Phase 2) | Days between recommendation and activity completion |
| Win rate on coached opps | Track (Phase 2) | Opps with accepted next_best_action |
| Qualification gap closure rate | Track (Phase 2) | Blocking gaps resolved within 14 days |
| Stale deal recovery rate | ≥ 40% | At-risk opps with activity within 7 days of recommendation |
| MEDDIC completeness (late stage) | Trending up | Blocking gaps on Proposal+ opps |

## Objective → Metric Mapping

See [BUSINESS_OBJECTIVES.md](BUSINESS_OBJECTIVES.md) for DECISION_MODEL factor to KPI linkage.

```yaml
metrics_version: "1.1.0"
agent_id: sales-rep
decision_model_weights_sum: 100
primary_artifacts: [opportunity_summary, next_best_action, qualification_gaps]
```
