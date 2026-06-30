# Business Objectives

Drives [DECISION_MODEL.md](DECISION_MODEL.md) weights and [METRICS.md](METRICS.md) business KPIs.

## Objectives

### 1. Accelerate Meeting Preparedness

**Outcome:** Reps and managers enter customer meetings with complete, CRM-grounded context in minutes instead of hours.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Brief completeness | Depth of CRM gather sequence | Brief completeness ≥ 90% |
| Meeting prep structure | MEETING_PREPARATION template | Meeting prep adoption ≥ 60% |
| Activity recency in brief | query_activities recency filter | Meeting prep time saved (survey) |

### 2. Improve Discovery Quality

**Outcome:** Discovery conversations close qualification gaps identified in CRM.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| SPIN question relevance | missing_data → question mapping | Research question usefulness ≥ 75% |
| Gap-targeted questions | DISCOVERY_PLAYBOOK alignment | Qualification gap closure (Phase 2) |
| Stakeholder-specific prompts | relationship_map role labels | Question acceptance rate |

### 3. Surface Revenue and Retention Risk Early

**Outcome:** Buying signals and service risks visible before deals stall or customers churn.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| CUSTOMER_RISK_GUIDE application | Risk priority weight 0.9 | Risk flag precision ≥ 85% |
| Case-opp correlation | P1/P2 + renewal/expansion pattern | Service-risk early detection |
| Buying signal detection | Stage progression, new opp events | Expansion signal conversion (Phase 2) |

### 4. Enable Strategic Account Visibility

**Outcome:** Managers and reps share a consistent account narrative for tier-1 accounts.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| ACCOUNT_PLANNING alignment | Tier, white-space, 90-day objectives | Pipeline influenced on researched accounts |
| Source grounding | source_records audit trail | Source grounding ≥ 98% |
| Assumption transparency | assumptions + missing_data | Zero hallucination incidents |

## Objective → Weight Mapping (DECISION_MODEL)

```text
Sales Velocity        ← Objective 1 (meeting prep)
Revenue               ← Objective 3 (buying signals)
Customer Retention    ← Objective 3 (service risks)
Manager Visibility    ← Objective 4 (strategic briefs)
Activity Effectiveness ← Objective 2 (research questions)
```

```yaml
business_objectives_version: "1.0.0"
agent_id: account-research
objectives:
  - id: meeting_prep_acceleration
    weight: 1.0
  - id: discovery_quality
    weight: 0.9
  - id: risk_surfacing
    weight: 0.9
  - id: strategic_visibility
    weight: 0.75
```
