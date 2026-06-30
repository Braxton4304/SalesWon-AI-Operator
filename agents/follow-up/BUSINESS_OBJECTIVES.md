# Business Objectives

Drives [DECISION_MODEL.md](DECISION_MODEL.md) weights and [METRICS.md](METRICS.md) business KPIs.

## Objectives

### 1. Accelerate Sales Velocity

**Driver:** Overdue activities and stale opps delay pipeline progression.

**Decision factors:** overdue_severity, close_date_proximity, stale cadence breach

**KPIs:** Overdue recovery rate within 48h; avg days from stale flag to next activity (Phase 2)

### 2. Maximize Activity Effectiveness

**Driver:** Generic or mistimed follow-ups waste rep capacity and annoy buyers.

**Decision factors:** activity_type_weight, EMAIL_LIBRARY template selection, objection-aware framing

**KPIs:** Email draft acceptance ≥ 65%; cadence recommendation usefulness ≥ 75%

### 3. Protect Revenue at Risk

**Driver:** High-value deals with silent periods slip or die.

**Decision factors:** revenue_weight (amount × probability), follow_up_priority critical threshold

**KPIs:** Revenue at risk touched after critical recommendation (Phase 2); false-negative overdue on closing opps → 0 tolerance in QA

### 4. Maintain CRM Discipline

**Driver:** Hygiene follow-ups keep data trustworthy for manager forecast.

**Decision factors:** ACTIVITY_PRIORITIZATION hygiene tier, missing_data surfacing

**KPIs:** False-positive overdue ≤ 5%; missing_data disclosure rate 100% when fields absent

## Objective → Weight Map

| Objective | DECISION_MODEL weight | BUSINESS_REASONING |
|-----------|----------------------|-------------------|
| Sales velocity | overdue + close_date = 60% of score | Primary |
| Activity effectiveness | template + timing quality | Primary |
| Revenue protection | revenue_weight = up to 30 points | Secondary |
| CRM discipline | hygiene tier for low scores | Supporting |

## Demo Narrative

Enterprise buyers expect the Follow-Up Agent to answer: *"Show me what I'm behind on, tell me what matters most, and give me a draft I can send in two minutes"* — without the AI sending on its own. Objectives 1–3 support that narrative; Objective 4 supports trust with managers auditing recommendations.

```yaml
business_objectives_version: "1.0.0"
agent_id: follow-up
objectives: [sales_velocity, activity_effectiveness, revenue_protection, crm_discipline]
```
