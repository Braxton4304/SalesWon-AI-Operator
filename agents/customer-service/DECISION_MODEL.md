# Decision Model

Agent-specific prioritization. **Runtime [DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) governs** — this file adjusts weights within allowed actions.

## Priority Order

1. **SLA safety** — Breach risk within 4 hours overrides informational requests
2. **ITIL severity** — High impact + high urgency cases before routine status checks
3. **Customer sentiment** — Escalated/angry cases before neutral status checks per CUSTOMER_SERVICE_FRAMEWORK
4. **Data completeness** — Retrieve case + account before drafting
5. **User explicit request** — Honor direct ask (e.g. "draft only") over proactive suggestions

## Scenario Matrix

| Scenario | Action | Rationale |
|----------|--------|-----------|
| Case number provided, record found | answer or recommend | High confidence |
| Case number missing | ask | Required for grounding |
| Case found, SLA < 2h to breach, no recent activity | recommend + escalation_required | Retention + SLA |
| High impact + high urgency inferred | answer with severity critical/high | ITIL matrix |
| Customer asks for refund | refuse + escalate | LIMITATIONS |
| Duplicate cases detected | answer + recommend merge review | Data quality |
| KB article may resolve | retrieve → answer | Avoid unnecessary escalation |
| VIP account + frustrated sentiment | escalation_required per ESCALATION.md | CUSTOMER_SERVICE_FRAMEWORK |
| Confidence < 0.60 after 3 retrieves | escalate | escalation-framework |

## Weighted Priority Formula (100%)

Used to compute `severity` ranking and sort account-level case lists. ITIL-aligned per ServiceNow CSM conventions.

```text
priority_score = Σ (factor_weight × normalized_factor_score)

Where normalized_factor_score ∈ [0.0, 1.0] per factor and weights sum to 100%:
```

| Factor | Weight | Normalization (0–1) | Source |
|--------|--------|---------------------|--------|
| **ITIL Impact** | 35% | high=1.0, medium=0.60, low=0.30 | case.impact or inferred from scope |
| **ITIL Urgency** | 30% | high=1.0, medium=0.60, low=0.30 | case.urgency or inferred from time sensitivity |
| **SLA proximity** | 15% | breached=1.0, at_risk(<4h)=0.85, at_risk(<24h)=0.60, on_track=0.20, n/a=0.10 | case SLA timers |
| **Customer sentiment** | 10% | angry=1.0, frustrated=0.70, neutral=0.30, positive=0.10, unknown=0.40 | case text + history |
| **Account strategic tier** | 10% | VIP/strategic=1.0, standard=0.50, low=0.20 | account tier flag |

**Verification:** 35 + 30 + 15 + 10 + 10 = **100%**

### ITIL Impact Levels

| Level | Definition | Normalized |
|-------|------------|------------|
| **High** | Enterprise-wide or revenue-critical service degradation | 1.0 |
| **Medium** | Department or team-level impact | 0.60 |
| **Low** | Single user or non-critical function | 0.30 |

### ITIL Urgency Levels

| Level | Definition | Normalized |
|-------|------------|------------|
| **High** | Immediate business impact; workaround unavailable | 1.0 |
| **Medium** | Needed soon; partial workaround exists | 0.60 |
| **Low** | Can schedule; minimal business disruption | 0.30 |

### Severity Derivation

Map `priority_score` to OUTPUT_SCHEMA `severity`:

| priority_score | severity |
|----------------|----------|
| ≥ 0.75 | critical |
| 0.55 – 0.74 | high |
| 0.35 – 0.54 | medium |
| < 0.35 | low |

When case.priority is set in ServiceNow, cross-check: if CRM priority conflicts with computed severity by more than one band, reduce confidence and note in missing_data.

### Worked Example

Case: high impact (production outage), high urgency (no workaround), SLA at_risk 3h remaining, frustrated sentiment, VIP account.

```text
= 0.35×1.0 + 0.30×1.0 + 0.15×0.85 + 0.10×0.70 + 0.10×1.0
= 0.35 + 0.30 + 0.1275 + 0.07 + 0.10
= 0.948 → severity: critical
```

## Tradeoffs

- **Speed vs. completeness:** Always retrieve case once; second retrieve only for linked records or KB
- **Draft length:** Default concise per EMAIL_STYLE_GUIDE; expand only if user asks for detailed reply
- **Inferred ITIL vs. CRM fields:** Prefer case.impact and case.urgency when present; infer from description only with confidence penalty

## Business Reasoning Weights

Aligns with runtime BUSINESS_REASONING — customer service agent emphasis:

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Customer Retention | 1.0 | Primary agent mandate |
| Manager Visibility | 0.85 | SLA and severity reporting |
| Revenue | 0.60 | Strategic account service risk signals only |
| Activity Effectiveness | 0.70 | Follow-up task recommendations |
| Sales Velocity | 0.30 | Out of scope — handoff only |

## Cannot Override

- governance-spec confidence thresholds
- data-spec case `missing_data_behavior: escalate` when required fields absent after retrieve
- escalation-framework mandatory triggers
- CUSTOMER_SERVICE_FRAMEWORK resolve-at-lowest-tier before escalation

```yaml
decision_model_version: "1.0.0"
agent_id: customer-service
priority_formula_weights_sum: 100
factors:
  - itil_impact: 35
  - itil_urgency: 30
  - sla_proximity: 15
  - customer_sentiment: 10
  - account_strategic_tier: 10
itil_aligned: true
```
