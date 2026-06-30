# Trust Model

**Why trust this recommendation?**

## Evidence Sources

| Source | Used For | Precedence |
|--------|----------|------------|
| ServiceNow opportunity | Amount, stage, probability, close_date, next_step, owner | Authoritative |
| ServiceNow activity | Engagement recency, rep cadence | Authoritative |
| ServiceNow contact | Stakeholder names, roles (MEDDIC mapping) | Authoritative |
| ServiceNow account | Tier, industry, linked cases | Authoritative |
| ServiceNow lead | Pre-opp qualification status | Authoritative |
| ServiceNow case | Service risk on active deal accounts | Authoritative |
| PIPELINE_HEALTH_MODEL | deal_health signal definitions | Policy |
| SALES_METHODOLOGIES | MEDDIC/SPIN/Sandler gap definitions | Methodology |
| SALES_PLAYBOOK | Objection handling, discovery guidance | Methodology |
| ACTIVITY_PRIORITIZATION | Action type ranking | Methodology |
| Knowledge base (RAG) | Product capabilities, battlecards | Supplementary |

Precedence per [data-spec](../../specifications/data-spec.md): CRM > Layer 4 config > policy/methodology > RAG > agent inference (never for CRM field values).

## Confidence Calculation

Per [shared/confidence-scoring.md](../../shared/confidence-scoring.md) adapted for rep scope:

| Factor | Impact |
|--------|--------|
| Opportunity retrieved with all required fields (amount, probability, close_date, owner) | +0.15 |
| Activities retrieved for opp | +0.10 |
| Contacts retrieved with role labels | +0.08 |
| ≥80% MEDDIC elements evidenced in CRM (late stage) | +0.10 |
| Account context retrieved when meeting prep requested | +0.05 |
| All financial assertions reconcile source_records | +0.10 |
| Missing amount or close_date | −0.20 |
| >21 days since last activity with no explanation | −0.08 |
| Stakeholder roles inferred (not confirmed) | −0.05 per role |
| Conflicting activity vs. opp next_step | −0.10 |
| Required retrieve failed after 3 attempts | −0.25 → escalate |
| User-provided account_brief without CRM re-verify | −0.05 |

## Confidence Bands

| Band | Range | Behavior |
|------|-------|----------|
| High | ≥ 0.85 | Full answer; suggested_follow_up ready for rep review |
| Medium | 0.60–0.84 | Answer with missing_data prominent; note inferred roles |
| Low | < 0.60 | Retrieve (up to 3x) then escalate |

## Missing Data / Assumptions

- **missing_data:** Required opp fields absent, contacts not linked, activity history incomplete — always list with impact on priority_score and deal_health
- **No assumptions array:** Rep agent does not infer CRM field values — use qualification_gaps, recommended_questions, and reduce confidence instead
- **source_records:** Field-level audit trail with confidence label (confirmed | inferred | unknown) for every factual assertion
- **Inferred roles:** contact role_label marked inferred in source_records when not explicitly in CRM

## Trust Signals for Users

1. Every deal financial traceable to opportunity source_record
2. qualification_gaps cite methodology (MEDDIC/SPIN/Sandler) and CRM field
3. priority_score explainable via DECISION_MODEL weight table (sums 100%)
4. next_best_action.rationale links to specific CRM evidence
5. recommended_questions address documented gaps — not generic scripts
6. escalation_required aligns with ESCALATION.md — never hidden in prose
7. suggested_follow_up clearly labeled draft — rep sends in ServiceNow

```yaml
trust_model_version: "1.1.0"
agent_id: sales-rep
confidence_framework: shared/confidence-scoring.md
decision_model_weights_sum: 100
methodologies: [meddic, spin, sandler]
```
