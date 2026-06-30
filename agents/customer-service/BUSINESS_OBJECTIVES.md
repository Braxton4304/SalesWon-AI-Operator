# Business Objectives

Drives [DECISION_MODEL.md](DECISION_MODEL.md) weights and [METRICS.md](METRICS.md) business KPIs.

## Objectives

### 1. Protect SLA Compliance and Customer Trust

**Outcome:** Reps respond before SLA breach with accurate status and empathetic communication.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| SLA early warning | SLA proximity 15% | Flag at-risk ≥ 24h before breach |
| Sentiment acknowledgment | Customer sentiment 10% | Acknowledgment in 100% of frustrated-case drafts |
| Draft quality | suggested_customer_response | Draft acceptance ≥ 70% |

### 2. Accurate ITIL Prioritization

**Outcome:** Cases receive consistent impact/urgency assessment aligned with ServiceNow priority.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Impact assessment | ITIL Impact 35% | ITIL alignment ≥ 90% vs. CRM priority |
| Urgency assessment | ITIL Urgency 30% | Severity formula compliance ≥ 90% |
| Priority transparency | priority_score in case_summary | Rep override rate trending down |

### 3. Reduce Mean Time to Meaningful Response

**Outcome:** Reps spend less time gathering context and drafting first responses.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Structured case_summary | case_summary artifact | First-response prep time −30% (survey) |
| Pre-built drafts | suggested_customer_response | Draft acceptance rate |
| Related case visibility | account case list pattern | Multi-case triage time reduction |

### 4. Appropriate Escalation at Lowest Tier

**Outcome:** Cases escalate only when CUSTOMER_SERVICE_FRAMEWORK and escalation-framework require it.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| Resolve at lowest tier | CUSTOMER_SERVICE_FRAMEWORK | Inappropriate escalation < 5% |
| VIP handling | Account strategic tier 10% | VIP-SENTIMENT trigger accuracy |
| Mandatory triggers | ESCALATION.md | Zero missed mandatory escalations |

### 5. Enable Cross-Functional Service Visibility

**Outcome:** Sales and workforce agents consume reliable case context for revenue and routing decisions.

| Driver | Decision Factor | KPI |
|--------|-----------------|-----|
| case_summary artifact | source_records audit | Source grounding ≥ 98% |
| Service risk signal | severity + escalation flags | Sales Manager cites without correction (Phase 2) |
| Confidence transparency | TRUST_MODEL bands | Zero hallucination incidents |

## Objective → Weight Mapping (DECISION_MODEL)

```text
Customer Retention    ← Objective 1 (SLA + sentiment) — BUSINESS_REASONING 1.0
ITIL Accuracy         ← Objective 2 (impact/urgency) — impact 35% + urgency 30%
Response Speed        ← Objective 3 (case_summary + drafts) — sla_proximity 15%
Escalation Discipline ← Objective 4 (lowest tier) — account tier 10% + escalation rules
Cross-Functional      ← Objective 5 (artifact quality) — source_records + case_summary
```

## Objective → DECISION_MODEL Factor Mapping

```text
SLA compliance        ← sla_proximity (15%) + escalation triggers
ITIL prioritization   ← itil_impact (35%) + itil_urgency (30%)
Customer empathy      ← customer_sentiment (10%)
Strategic accounts    ← account_strategic_tier (10%)
Severity derivation   ← priority_score → severity bands
```

```yaml
business_objectives_version: "1.0.0"
agent_id: customer-service
objectives:
  - id: sla_compliance_and_trust
    weight: 1.0
  - id: itil_prioritization
    weight: 0.95
  - id: response_speed
    weight: 0.90
  - id: escalation_discipline
    weight: 0.85
  - id: cross_functional_visibility
    weight: 0.80
decision_model_weights_sum: 100
factors:
  itil_impact: 35
  itil_urgency: 30
  sla_proximity: 15
  customer_sentiment: 10
  account_strategic_tier: 10
```
