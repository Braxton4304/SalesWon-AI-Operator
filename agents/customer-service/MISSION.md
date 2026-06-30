# Mission

**Primary outcome:** Reduce mean time to meaningful first response and resolution prep while maintaining SLA compliance, accurate ITIL prioritization, and customer trust.

## Success Criteria

- Case summary accuracy ≥ 95% verified against ServiceNow on audit sample
- Draft acceptance rate ≥ 70% used with minor or no edits
- SLA breach prevention — flag at-risk cases ≥ 24h before breach when SLA data available
- Escalation appropriateness ≤ 5% inappropriate escalations
- ITIL impact/urgency assessments align with case priority on ≥ 90% of audit sample
- Source grounding ≥ 98% of factual claims in source_records

## Business Reasoning Alignment

Per [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md):

- **Customer Retention** — Primary. Sentiment-aware responses, SLA safety, and proactive escalation flags per CUSTOMER_SERVICE_FRAMEWORK.
- **Manager Visibility** — Secondary. SLA status, severity, and case backlog summaries on request.
- **Revenue** — Tertiary. Identifies service-risk signals on strategic accounts for human handoff to sales; does not sell.

## ServiceNow Context

Operates on CSM tables: `sn_customerservice_case` (mapped as **case** in data-spec), linked **account**, **contact**, and **activity** records.

```yaml
mission_version: "1.0.0"
agent_id: customer-service
primary_outcome: faster_meaningful_response_with_sla_compliance
primary_artifacts: [case_summary, suggested_customer_response]
```
