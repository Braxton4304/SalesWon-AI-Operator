# Customer Promises Policy

Agents MUST NOT promise customers:

- Pricing, discounts, or credits
- Refunds or billing adjustments
- Legal or contractual terms
- Delivery dates or SLAs not confirmed in CRM/policy
- Product capabilities not in approved KB
- Case/opportunity resolution timelines not backed by SLA data

Violations → `decision_action: refuse` or `escalate` per agent ESCALATION.md.

```yaml
policy_id: customer_promises
enforcement: refuse_or_escalate
kb_grounding_required_for_product_claims: true
```
