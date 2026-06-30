# Business Objectives

Drives [DECISION_MODEL.md](DECISION_MODEL.md) weights and [METRICS.md](METRICS.md) business KPIs.

## Objectives

### 1. Accelerate Deal Progression

**Outcome:** Reps act on the highest-impact opportunity activities before close-date windows close.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Close-date urgency | Close-date weight 30% | Stale deal recovery rate ≥ 40% |
| Revenue prioritization | Revenue at stake 20% | Pipeline velocity (Phase 2) |
| Activity timing | Activity recency 15% | Days between recommendation and logged activity |

### 2. Improve Qualification Rigor

**Outcome:** Late-stage deals have documented MEDDIC coverage — reducing surprise losses.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| MEDDIC gap detection | Qualification gap severity 15% | Qualification gap usefulness ≥ 80% |
| Discovery quality | SPIN recommended_questions | Gap closure rate within 14 days (Phase 2) |
| Budget/decision clarity | Sandler checks in Proposal+ | Blocking gaps on Proposal+ opps trending down |

### 3. Increase Rep Activity Effectiveness

**Outcome:** Reps spend time on CRM-grounded next actions that advance deals — not generic busywork.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Next-best-action ranking | DECISION_MODEL priority_score | Next-best-action acceptance ≥ 65% |
| Follow-up quality | suggested_follow_up drafts | Draft acceptance ≥ 60% |
| User focus | User explicit focus 10% | Repeat deal review rate (lower is better) |

### 4. Strengthen Deal Health Visibility

**Outcome:** Reps recognize at-risk deals early and take corrective action.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Health scoring | Deal health severity 10% | At-risk opps with action within 7 days |
| Source transparency | source_records audit trail | Source grounding ≥ 98% |
| Confidence honesty | TRUST_MODEL bands | Zero hallucination incidents |

### 5. Enable Manager and Team Handoffs

**Outcome:** opportunity_summary artifacts support manager coaching and follow-up cadence without duplicate rep work.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Artifact quality | opportunity_summary completeness | Handoff citation rate (Phase 2) |
| Escalation discipline | escalation_required accuracy | Escalation precision ≥ 95% |
| Collaboration | COLLABORATION.md handoffs | Manager coaching alignment survey |

## Objective → Weight Mapping (DECISION_MODEL)

```text
Revenue               ← Objective 1 (deal progression) — BUSINESS_REASONING 1.0
Sales Velocity        ← Objective 1 (close-date urgency) — BUSINESS_REASONING 1.0
Activity Effectiveness ← Objective 3 (next-best-action) — BUSINESS_REASONING 0.9
Qualification Rigor   ← Objective 2 (MEDDIC/SPIN/Sandler) — qualification_gap_severity 15%
Deal Health           ← Objective 4 (early risk detection) — deal_health_severity 10%
Manager Visibility    ← Objective 5 (handoffs) — BUSINESS_REASONING 0.70
```

## Objective → DECISION_MODEL Factor Mapping

```text
Deal progression       ← close_date_urgency (30%) + revenue_at_stake (20%)
Qualification rigor    ← qualification_gap_severity (15%) + recommended_questions
Activity effectiveness ← activity_recency_gap (15%) + next_best_action
Early risk detection   ← deal_health_severity (10%)
Rep focus              ← user_explicit_focus (10%)
```

## Methodology → Objective Mapping

| Methodology | Primary Objective | Stage |
|-------------|-------------------|-------|
| SPIN | Qualification rigor + deal progression | Discovery |
| MEDDIC | Qualification rigor + deal health | Qualification / Proposal |
| Sandler | Qualification rigor (pain/budget/decision) | Mid / late stage |

```yaml
business_objectives_version: "1.1.0"
agent_id: sales-rep
objectives:
  - id: deal_progression
    weight: 1.0
  - id: qualification_rigor
    weight: 0.95
  - id: activity_effectiveness
    weight: 0.90
  - id: deal_health_visibility
    weight: 0.85
  - id: team_handoffs
    weight: 0.80
decision_model_weights_sum: 100
methodologies: [meddic, spin, sandler]
```
