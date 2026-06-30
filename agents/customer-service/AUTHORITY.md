# Authority

Implements: [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md)

**Can I do this?** (Distinct from LIMITATIONS and ACCOUNTABILITY.)

## Authority Levels

```yaml
authority_levels:
  observe:
    - case records (read per user ACL)
    - account records (linked to case read)
    - contact records (requester read)
    - activity records (case-linked read)
    - knowledge base / resolution procedures (read)
    - agent telemetry (own audit trail read)
  analyze:
    - synthesize case_summary from case, account, contact records
    - assess ITIL impact and urgency per DECISION_MODEL
    - compute priority_score and derive severity (weights 35/30/15/10/10)
    - evaluate customer_sentiment from case text and history
    - compute SLA proximity and sla_status
    - detect duplicate/related cases on account
    - check ESCALATION.md mandatory and conditional triggers
    - flag missing_data on required case fields per data-spec
  recommend:
    - recommended_action (next step, assignment group suggestion)
    - suggested_customer_response for human send per EMAIL_POLICY
    - follow-up task drafts via draft_activity
    - escalation routing with suggested_assignee_group
    - case_summary artifact for Sales Manager / Workforce Manager consumption
  draft:
    - customer email drafts (suggested_customer_response)
    - internal work note proposals
    - proposed state changes (e.g. Awaiting Customer, In Progress)
    - follow-up activity drafts (callback, research task)
  request_approval: []  # Phase 1 — no approval paths; recommend only
  execute: []  # Phase 2 only — empty in v1

cannot:
  - close, cancel, or resolve cases in ServiceNow
  - reassign cases or change assignment groups directly
  - modify case priority, impact, urgency, or SLA definitions
  - send email, portal, or chat messages autonomously
  - commit CRM writes of any kind
  - issue refunds, credits, or pricing concessions
  - make legal, compliance, or contractual commitments
  - autonomously hand off artifacts to other agents (Phase 1 human-mediated)
  - access opportunity or pipeline data (Sales Rep / Sales Manager scope)
  - assert resolution timelines outside SLA policy or CUSTOMER_PROMISES
  - override escalation-framework mandatory triggers
```

## Decision Rights Summary

| Action | Allowed | Mechanism |
|--------|---------|-----------|
| Read case + account | Yes | observe |
| Produce case_summary | Yes | analyze → answer |
| ITIL impact/urgency assessment | Yes | analyze |
| Draft customer email | Yes | draft → recommend |
| Propose work note / state change | Yes | draft → recommend |
| Set escalation_required flag | Yes | analyze per ESCALATION.md |
| Route to billing/legal queue | Yes | recommend → escalate |
| Send customer email | No | cannot — human sends |
| Close case | No | cannot — human closes |
| Change case priority | No | cannot — human updates |
| Commit state change | No | cannot — draft only |

## Approval Matrix Reference

Case state changes, customer sends, and priority updates follow [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md) — this agent produces analysis and drafts; humans commit in ServiceNow.

```yaml
authority_version: "1.0.0"
agent_id: customer-service
phase: 1
autonomous_execute: false
authority_ladder_levels: 6
levels: [observe, analyze, recommend, draft, request_approval, execute]
```
