# Trust Model

**Why trust this recommendation?**

## Evidence Sources

| Source | Used For | Precedence |
|--------|----------|------------|
| ServiceNow team_pipeline_view | Aggregate pipeline, quota, period metrics | Authoritative |
| ServiceNow opportunity | Amount, stage, probability, close_date, forecast category, owner | Authoritative |
| ServiceNow activity | Engagement recency, rep cadence | Authoritative |
| ServiceNow account | Tier, strategic value for weighting | Authoritative |
| ServiceNow case | Service risk on forecast accounts | Authoritative |
| PIPELINE_HEALTH_MODEL | Deal health signal definitions | Policy |
| PIPELINE_INSPECTION_GUIDE | Hygiene checklist, coaching standards | Policy |
| EXECUTIVE_SUMMARY_STANDARD | Brief structure | Methodology |
| CUSTOMER_RISK_GUIDE | Service risk severity in forecast context | Policy |
| SALES_PLAYBOOK ch. 9–10 | Forecasting and customer risk context | Methodology |
| Knowledge base (RAG) | Coaching language, inspection procedures | Supplementary |

Precedence per [data-spec](../../specifications/data-spec.md): CRM > Layer 4 config > policy/methodology > RAG > agent inference (never for CRM field values).

## Confidence Calculation

Per [shared/confidence-scoring.md](../../shared/confidence-scoring.md) adapted for manager scope:

| Factor | Impact |
|--------|--------|
| Team pipeline view retrieved with current period | +0.12 |
| Quota available for coverage ratio | +0.08 |
| ≥90% commit opps with required fields complete | +0.10 |
| Activities retrieved for all at-risk commit opps | +0.08 |
| Case data retrieved when service_risk signal used | +0.05 |
| All pipeline totals reconcile opp sum vs. team view | +0.10 |
| Missing quota (coverage unavailable) | −0.10 |
| >20% commit opps missing required fields | −0.15 |
| Team view stale (>24h) or partial pagination | −0.12 |
| Conflicting opp vs. team view totals | −0.20 → escalate |
| Manager scope ambiguous (resolved via ask) | −0.05 |

## Confidence Bands

| Band | Range | Behavior |
|------|-------|----------|
| High | ≥ 0.85 | Full answer; executive brief ready for forecast call |
| Medium | 0.60–0.84 | Answer with missing_data prominent; note coverage/quota gaps |
| Low | < 0.60 | Retrieve (up to 3x) then escalate |

## Missing Data / Assumptions

- **missing_data:** Quota absent, incomplete team view, required opp fields missing — always list with impact on coverage or risk scoring
- **No assumptions array:** Manager agent does not infer CRM field values — use missing_data and reduce confidence instead
- **source_records:** Field-level audit trail for every pipeline total, risk claim, and coaching evidence

## Trust Signals for Users

1. Every pipeline total traceable to team_pipeline_view or opp source_record
2. forecast_risks.signals cite PIPELINE_HEALTH_MODEL signal names
3. priority_score explainable via DECISION_MODEL weight table (sums 100%)
4. rep_coaching_items link to opportunity_ids and activity evidence
5. data_hygiene_issues reference PIPELINE_INSPECTION_GUIDE checklist_item
6. coverage_ratio null when quota unavailable — never estimated

```yaml
trust_model_version: "1.0.0"
agent_id: sales-manager
confidence_framework: shared/confidence-scoring.md
decision_model_weights_sum: 100
```
