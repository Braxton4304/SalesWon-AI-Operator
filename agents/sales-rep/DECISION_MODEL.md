# Decision Model

Agent-specific prioritization. **Runtime [DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) governs** — this file adjusts weights within allowed actions.

Implements: [shared/SALES_METHODOLOGIES.md](../../shared/SALES_METHODOLOGIES.md), [shared/ACTIVITY_PRIORITIZATION.md](../../shared/ACTIVITY_PRIORITIZATION.md)

## Priority Order

1. **Close-date proximity** — Deals closing within 14 days first
2. **Revenue weight** — amount × probability (ROI_SCORING_MODEL)
3. **Qualification gap severity** — MEDDIC/SPIN/Sandler blocking gaps on late-stage opps
4. **Deal hygiene gaps** — Missing next_step or stale activity on high-value opps
5. **User explicit focus** — Named opportunity overrides generic queue
6. **Activity effectiveness** — ROI-weighted action type per ACTIVITY_PRIORITIZATION

## Scenario Matrix

| Scenario | Action |
|----------|--------|
| Opp number/name given, record found | answer with full OUTPUT_SCHEMA |
| "My pipeline today" | query user's open opps → ranked next_best_action list |
| Missing economic buyer in late stage | recommend stakeholder activity + recommended_questions (MEDDIC) |
| Early-stage discovery request | SPIN recommended_questions + Sandler pain funnel |
| Pricing/discount request | refuse commitment → escalation_required + escalate |
| Objection handling | answer from playbook + CRM context |
| Required opp fields missing | ask or retrieve related account data → missing_data |
| Multiple opp name matches | ask with candidate list |
| Confidence < 0.60 after 3 retrieves | escalate per ESCALATION.md |
| Manager coaching conflict | note rep_coaching_items context; defer to manager guidance |

## Methodology Selection (MEDDIC / SPIN / Sandler)

| Opp Stage | Primary | Secondary | qualification_gaps Focus |
|-----------|---------|-----------|--------------------------|
| Lead / Prospecting | SPIN | Sandler upfront contract | Situation, Problem, pain identification |
| Discovery / Qualification | MEDDIC | SPIN Implication/Need-payoff | Metrics, Pain, Champion, Economic Buyer |
| Proposal / Negotiation | MEDDIC | Sandler budget/decision | Decision Criteria, Decision Process, Economic Buyer |
| Closed / N/A | CRM hygiene only | — | not_applicable |

### MEDDIC Field Mapping

| Element | CRM / Evidence Source | Gap Severity Rule |
|---------|----------------------|-------------------|
| Metrics | opp metrics field, activity notes | blocking in Proposal+ if absent |
| Economic Buyer | contact role economic_buyer | blocking in Qualification+ if absent |
| Decision Criteria | opp description, activity | important in Proposal |
| Decision Process | activity, next_step | important in Proposal |
| Identify Pain | activity, opp description | blocking if late stage with no pain documented |
| Champion | contact role champion | blocking in Qualification+ if absent |

### SPIN Question Types (recommended_questions)

| Type | When | Example Direction |
|------|------|-------------------|
| Situation | Early discovery | Current process, tools, team structure |
| Problem | Pain not documented | Explicit pain and impact questions |
| Implication | Problem identified | Cost of inaction, downstream effects |
| Need-payoff | Solution fit emerging | Value of resolving pain with solution |

### Sandler Checks

| Check | Signal | Gap if Missing |
|-------|--------|----------------|
| Upfront contract | Meeting purpose agreed | important in early stage |
| Pain | Documented compelling event | blocking in mid/late stage |
| Budget | Budget authority discussed | blocking in Proposal |
| Decision | Decision timeline and steps | important in Proposal |

## Weighted Priority Formula (100%)

Used to rank `next_best_action.priority_score` and "what should I do today" pipeline lists.

```text
priority_score = Σ (factor_weight × normalized_factor_score)

Where normalized_factor_score ∈ [0.0, 1.0] per factor and weights sum to 100%:
```

| Factor | Weight | Normalization (0–1) | Source |
|--------|--------|---------------------|--------|
| **Close-date urgency** | 30% | max(0, 1 − days_to_close / 90); slipped dates = 1.0 | opp.close_date |
| **Revenue at stake** | 20% | min(opp.amount × opp.probability / rep_top_weighted_opp, 1.0) | opp.amount, opp.probability |
| **Qualification gap severity** | 15% | blocking=1.0, important=0.6, nice_to_have=0.2, none=0.0 (worst gap wins) | MEDDIC/SPIN/Sandler gaps |
| **Activity recency gap** | 15% | min(days_since_activity / 21, 1.0) | activity |
| **Deal health severity** | 10% | critical=1.0, at_risk=0.65, healthy=0.2, unknown=0.5 | PIPELINE_HEALTH_MODEL |
| **User explicit focus** | 10% | named opp in request=1.0; pipeline queue=0.3 | user request |

**Verification:** 30 + 20 + 15 + 15 + 10 + 10 = **100%**

### Worked Example

Opp: $120K at 45% ($54K weighted), closes in 12 days, 18 days since activity, blocking MEDDIC gap (economic_buyer), at_risk health, user named this opp.

```text
= 0.30×0.867 + 0.20×0.675 + 0.15×1.0 + 0.15×0.857 + 0.10×0.65 + 0.10×1.0
= 0.260 + 0.135 + 0.150 + 0.129 + 0.065 + 0.100
= 0.839 (priority: high — schedule economic buyer engagement)
```

## Business Reasoning Weights

Aligns with runtime BUSINESS_REASONING — rep agent emphasis:

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Revenue | 1.0 | Primary — deal progression |
| Sales Velocity | 1.0 | Primary — activity timing |
| Activity Effectiveness | 0.9 | Next-best-action quality |
| Customer Retention | 0.75 | Service risk flags on active deals |
| Manager Visibility | 0.70 | opportunity_summary for manager handoffs |

## Cannot Override

- governance-spec confidence thresholds
- data-spec write permissions (draft_only)
- escalation-framework mandatory triggers
- PIPELINE_HEALTH_MODEL signal definitions without Layer 4 override
- SALES_METHODOLOGIES field definitions

```yaml
decision_model_version: "1.1.0"
agent_id: sales-rep
priority_formula_weights_sum: 100
methodologies: [meddic, spin, sandler]
factors:
  - close_date_urgency: 30
  - revenue_at_stake: 20
  - qualification_gap_severity: 15
  - activity_recency_gap: 15
  - deal_health_severity: 10
  - user_explicit_focus: 10
```
