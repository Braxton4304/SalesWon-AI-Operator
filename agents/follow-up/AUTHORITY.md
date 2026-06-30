# Authority

Implements: [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md)

**Can I do this?** (Distinct from LIMITATIONS and ACCOUNTABILITY.)

```yaml
authority_levels:
  observe:
    - activity.state
    - activity.due_date
    - activity.type
    - opportunity.stage
    - opportunity.close_date
    - opportunity.amount
    - account.tier
    - contact.name
    - contact.email
  analyze:
    - overdue_detection
    - stale_opportunity_detection
    - cadence_recommendation
    - follow_up_priority_scoring
    - objection_framing
  recommend:
    - follow_up_timing
    - activity_reprioritization
    - email_draft
    - call_script
    - next_activity_proposal
  draft:
    - activity.follow_up_task
    - email.customer_outreach
  request_approval:
    - escalation.pricing_objection
    - escalation.legal_language
    - escalation.strategic_account_critical
  execute: []  # Phase 2 only — empty in Phase 1
cannot:
  - send_email
  - send_sms
  - complete_activity
  - reassign_activity
  - update_opportunity_stage
  - commit_pricing
  - autonomous_queue_monitor
  - cross_tenant_read
```

## Authority Checks in Runtime

Before `decision_action: recommend` on email drafts, runtime validates draft_only per COMMUNICATION_STANDARD. Before customer-facing content referencing pricing, agent MUST set escalation_required and route via request_approval paths.

## Phase 1 Summary

| Action | Allowed |
|--------|---------|
| List overdue activities | Yes (observe + analyze) |
| Recommend timing and priority | Yes (recommend) |
| Draft email / task | Yes (draft → human approve) |
| Send email | No |
| Close overdue task | No |
