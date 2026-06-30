# Quality

Correctness, completeness, and hallucination avoidance criteria for this agent.

## Correctness

- [ ] Pipeline totals match team_pipeline_view or summed opp records in manager scope
- [ ] Weighted pipeline uses CRM probability × amount — not invented weighting rules
- [ ] Coverage ratio computed only when quota present in CRM or Layer 4 — otherwise null + missing_data
- [ ] Opportunity stage, amount, close_date, probability, forecast_category match opp records
- [ ] forecast_risks health signals map to PIPELINE_HEALTH_MODEL definitions
- [ ] priority_score aligns with DECISION_MODEL formula (weights sum 100%)
- [ ] rep_coaching_items cite verifiable opp/activity evidence with rep name
- [ ] data_hygiene_issues reference PIPELINE_INSPECTION_GUIDE checklist items
- [ ] Service risk claims cite case records per CUSTOMER_RISK_GUIDE
- [ ] Tenant and manager visibility rules respected

## Completeness

- [ ] All required OUTPUT_SCHEMA fields present (including empty arrays where applicable)
- [ ] pipeline_summary.metrics populated or gaps in missing_data
- [ ] forecast_risks include signals array and intervention_rationale for each entry
- [ ] top_intervention_opportunities ranked by priority_score (descending)
- [ ] rep_coaching_items include suggested_action for each coaching topic
- [ ] manager_actions numbered with owner and priority
- [ ] Executive brief includes all EXECUTIVE_SUMMARY_STANDARD sections when requested
- [ ] source_records cover all opps referenced in risks and coaching

## Hallucination Avoidance

- [ ] No pipeline totals without team_pipeline_view or opp source_records
- [ ] No quota or coverage targets invented when not in CRM/Layer 4
- [ ] No win rates or conversion benchmarks without approved Layer 4 baseline
- [ ] No rep performance judgments without CRM evidence
- [ ] No forecast category changes presented as committed — recommend only
- [ ] No external market or competitor claims in Phase 1

## Demo Scenarios

| # | Scenario | Expected Output |
|---|----------|-----------------|
| 1 | Full team pipeline Q3 review | Complete schema; pipeline_summary + forecast_risks + executive_brief |
| 2 | Commit deals at risk — 30-day window | forecast_risks filtered; top_intervention_opportunities ranked |
| 3 | Rep coaching — Jordan Lee | rep_coaching_items for Jordan; constructive evidence-linked |
| 4 | Pipeline hygiene on commit category | data_hygiene_issues with checklist_item references |
| 5 | Executive brief for forecast call | executive_brief per EXECUTIVE_SUMMARY_STANDARD |
| 6 | Coverage analysis — quota in CRM | coverage_ratio populated with source_records |
| 7 | Coverage analysis — no quota | coverage_ratio null; missing_data for quota |
| 8 | Ambiguous team scope | decision_action: ask with disambiguation |
| 9 | Forecast commit request | decision_action: refuse; explain human commit required |
| 10 | Service risk on forecast account | forecast_risks includes service_risk signal + case source_record |
| 11 | Team view incomplete after 3 retrieves | confidence < 0.60; decision_action: escalate |

## Evaluation Harness (Planned)

Automated validation against OUTPUT_SCHEMA + golden team pipeline datasets. See [architecture/domains/testing-deployment](../../architecture/domains/testing-deployment/README.md).

```yaml
quality_version: "1.0.0"
agent_id: sales-manager
demo_scenario_count: 11
```
