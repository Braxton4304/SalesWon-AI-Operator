# Mission

**Primary outcome:** Reduce time-to-preparedness for customer meetings and account reviews by delivering CRM-grounded account intelligence that reps and managers can act on immediately.

## Success Criteria

| Metric | Target (Phase 1 pilot) |
|--------|------------------------|
| Account brief completeness | ≥ 90% of requested sections populated from CRM |
| Source grounding rate | ≥ 98% of factual claims traceable to source_records |
| Research question usefulness | ≥ 75% rated useful per rep/manager survey |
| Meeting prep adoption | ≥ 60% of briefs used without major manual rewrite |
| Risk flag accuracy | ≥ 85% alignment with CUSTOMER_RISK_GUIDE signals |

## Business Reasoning Alignment

Per [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md):

- **Revenue** — Primary. Surfaces expansion white-space, open pipeline, and buying signals tied to opportunities.
- **Sales Velocity** — Primary. Accelerates meeting prep and discovery so reps spend less time assembling context.
- **Customer Retention** — Secondary. Flags service risk via case patterns per CUSTOMER_RISK_GUIDE.
- **Manager Visibility** — Secondary. Produces briefs consumable by Sales Manager Agent for strategic account reviews.
- **Activity Effectiveness** — Tertiary. Recommends targeted research questions that improve discovery quality.

## ServiceNow Context

Research draws from **account**, **contact**, **opportunity**, **case**, and **activity** objects. Account planning updates remain recommend-only per ACCOUNT_PLANNING.md — humans commit in CRM.
