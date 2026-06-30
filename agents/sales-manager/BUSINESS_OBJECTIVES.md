# Business Objectives

Drives [DECISION_MODEL.md](DECISION_MODEL.md) weights and [METRICS.md](METRICS.md) business KPIs.

## Objectives

### 1. Improve Forecast Accuracy

**Outcome:** Managers enter forecast calls with CRM-grounded visibility into commit risk and coverage — reducing surprise misses.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Commit risk detection | Forecast category exposure 25% | Forecast accuracy uplift (manager survey) |
| Priority ranking | DECISION_MODEL priority_score | At-risk commit intervention rate ≥ 70% |
| Coverage visibility | pipeline_summary.coverage_ratio | Coverage ratio available when quota in CRM |

### 2. Accelerate Manager Intervention

**Outcome:** Manager time targets the highest-impact deals before close-date windows close.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Intervention ranking | top_intervention_opportunities | Deal save rate (Phase 2 analytics) |
| Close-date urgency | Close-date weight 15% | Median days-to-intervention on critical risks |
| Executive brief readiness | EXECUTIVE_SUMMARY_STANDARD | Exec brief time saved (survey) |

### 3. Elevate Rep Coaching Effectiveness

**Outcome:** 1:1 conversations are evidence-led and constructive — improving rep pipeline discipline.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Evidence-linked coaching | rep_coaching_items.linked_opportunity_ids | Coaching usefulness ≥ 75% |
| Inspection checklist | PIPELINE_INSPECTION_GUIDE | Hygiene closure rate within sprint window |
| Balanced feedback | positive_recognition coaching_type | Rep engagement in 1:1 (survey) |

### 4. Strengthen Pipeline Data Hygiene

**Outcome:** Commit-category deals have complete required fields — enabling reliable health scores.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Required field detection | Data hygiene penalty 7% | Hygiene issue count trending down |
| Manager hygiene sprints | manager_actions hygiene type | Commit opp field completeness ≥ 95% |
| Forecast category alignment | PIPELINE_INSPECTION_GUIDE | Misaligned category count trending down |

### 5. Enable Executive Visibility

**Outcome:** Leadership receives consistent, CRM-sourced pipeline narratives for decision-making.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| EXECUTIVE_SUMMARY_STANDARD | pipeline_summary.executive_brief | Forecast call preparedness rating |
| Source grounding | source_records audit trail | Source grounding ≥ 98% |
| Confidence transparency | TRUST_MODEL bands | Zero hallucination incidents |

## Objective → Weight Mapping (DECISION_MODEL)

```text
Manager Visibility    ← Objective 5 (executive briefs) — BUSINESS_REASONING 1.0
Revenue               ← Objective 1 (forecast accuracy) — BUSINESS_REASONING 0.95
Sales Velocity        ← Objective 2 (intervention speed) — BUSINESS_REASONING 0.90
Activity Effectiveness ← Objective 3 (rep coaching) — BUSINESS_REASONING 0.85
Customer Retention    ← Service risk in forecast context — BUSINESS_REASONING 0.75
```

## Objective → DECISION_MODEL Factor Mapping

```text
Forecast accuracy     ← forecast_category_exposure (25%) + deal_health_severity (20%)
Intervention speed    ← close_date_urgency (15%) + revenue_at_stake (18%)
Rep coaching          ← activity_recency_gap (10%) + rep variance patterns
Data hygiene          ← data_hygiene_penalty (7%)
Retention risk        ← service_risk_correlation (5%)
```

```yaml
business_objectives_version: "1.0.0"
agent_id: sales-manager
objectives:
  - id: forecast_accuracy
    weight: 1.0
  - id: manager_intervention
    weight: 0.95
  - id: rep_coaching
    weight: 0.90
  - id: pipeline_hygiene
    weight: 0.85
  - id: executive_visibility
    weight: 0.80
decision_model_weights_sum: 100
```
