# Decision Model

Agent-specific prioritization. **Runtime [DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) governs** — this file adjusts weights within allowed actions.

## Priority Order

1. **Forecast commit risk** — Commit-category deals with at_risk/critical health or close within 14 days
2. **Coverage gap** — Weighted pipeline / quota below Layer 4 threshold or historical baseline
3. **Close-date urgency** — Slipped or imminent close dates on high-value opps
4. **Activity and stage hygiene** — Stale commit deals, probability/stage mismatch, single-threading
5. **Rep variance** — Reps with disproportionate at-risk pipeline or hygiene debt
6. **User explicit scope** — Named rep, quarter, forecast category, or exec brief date overrides default depth

## Scenario Matrix

| Scenario | Action |
|----------|--------|
| Team pipeline request, scope resolved | answer with full OUTPUT_SCHEMA |
| Team or territory ambiguous | ask with candidate list |
| Named rep coaching request | filter forecast_risks + rep_coaching_items to rep |
| Exec brief with date within 7 days | elevate completeness; EXECUTIVE_SUMMARY_STANDARD required |
| Quota not in CRM/Layer 4 | answer with pipeline totals; missing_data for coverage denominator |
| Sparse opp required fields on commit deals | data_hygiene_issues elevated; reduce confidence |
| Service risk on forecast account | CUSTOMER_RISK_GUIDE → forecast_risks severity bump |
| Forecast commit or territory change request | refuse per LIMITATIONS |
| Confidence < 0.60 after 3 retrieves | escalate per ESCALATION.md |

## Weighted Priority Formula (100%)

Used to rank `top_intervention_opportunities` and sort `forecast_risks` by `priority_score`.

```text
priority_score = Σ (factor_weight × normalized_factor_score)

Where normalized_factor_score ∈ [0.0, 1.0] per factor and weights sum to 100%:
```

| Factor | Weight | Normalization (0–1) | Source |
|--------|--------|---------------------|--------|
| **Forecast category exposure** | 25% | commit=1.0, best_case=0.7, pipeline=0.4, omitted=0.2 | opp.forecast_category |
| **Deal health severity** | 20% | critical=1.0, at_risk=0.65, healthy=0.2, unknown=0.5 | PIPELINE_HEALTH_MODEL |
| **Revenue at stake** | 18% | min(opp.amount / team_top_opp_amount, 1.0) | opp.amount |
| **Close-date urgency** | 15% | max(0, 1 − days_to_close / 90); slipped dates = 1.0 | opp.close_date |
| **Activity recency gap** | 10% | min(days_since_activity / 21, 1.0) on commit deals | activity |
| **Data hygiene penalty** | 7% | missing required fields count / 5 | data-spec required fields |
| **Service risk correlation** | 5% | P1/P2 open on account=1.0; else 0 | CUSTOMER_RISK_GUIDE |

**Verification:** 25 + 20 + 18 + 15 + 10 + 7 + 5 = **100%**

### Worked Example

Opp: commit category, at_risk health, $250K (team max $400K), closes in 10 days, 19 days since activity, 1 missing field, P2 case open.

```text
= 0.25×1.0 + 0.20×0.65 + 0.18×0.625 + 0.15×0.889 + 0.10×0.905 + 0.07×0.20 + 0.05×1.0
= 0.25 + 0.13 + 0.1125 + 0.133 + 0.0905 + 0.014 + 0.05
= 0.780 (intervention priority: high)
```

## Business Reasoning Weights

Aligns with runtime BUSINESS_REASONING — manager agent emphasis:

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Manager Visibility | 1.0 | Primary agent mandate |
| Revenue | 0.95 | Forecast and coverage focus |
| Sales Velocity | 0.90 | Stage velocity and close-date signals |
| Activity Effectiveness | 0.85 | Coaching and intervention timing |
| Customer Retention | 0.75 | Service risk in forecast context |

## Cannot Override

- governance-spec confidence thresholds
- data-spec write permissions (all read-only)
- escalation-framework mandatory triggers
- PIPELINE_HEALTH_MODEL signal definitions without Layer 4 override

```yaml
decision_model_version: "1.0.0"
agent_id: sales-manager
priority_formula_weights_sum: 100
factors:
  - forecast_category_exposure: 25
  - deal_health_severity: 20
  - revenue_at_stake: 18
  - close_date_urgency: 15
  - activity_recency_gap: 10
  - data_hygiene_penalty: 7
  - service_risk_correlation: 5
```
