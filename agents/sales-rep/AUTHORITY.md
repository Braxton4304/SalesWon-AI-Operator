# Authority

Implements: [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md)

**Can I do this?** (Distinct from LIMITATIONS and ACCOUNTABILITY.)

## Authority Levels

```yaml
authority_levels:
  observe:
    - opportunity records (rep-scoped read)
    - account records (linked to rep opps read)
    - contact records (linked to rep opps read)
    - activity records (rep opp and account read)
    - lead records (rep-scoped read)
    - case records (account context on active deals read)
    - knowledge base / playbook / methodology content (read)
    - agent telemetry (own audit trail read)
  analyze:
    - synthesize opportunity_summary from CRM objects
    - score deal_health per PIPELINE_HEALTH_MODEL
    - run MEDDIC/SPIN/Sandler qualification gap analysis
    - compute priority_score per DECISION_MODEL (weights sum 100%)
    - rank pipeline opps for "what should I do today"
    - generate recommended_questions by methodology and stage
    - assess objection handling context from playbook + CRM
    - flag missing_data on absent required fields
    - compute confidence per TRUST_MODEL
  recommend:
    - next_best_action with priority_score and due_within_days
    - suggested_follow_up (email draft, activity task, opp update proposal)
    - qualification gap remediation steps
    - meeting prep brief structure
    - lead conversion recommendation (human confirms)
    - opportunity_summary artifact for manager/follow-up consumption
    - CS escalation recommendation for service-risk deals
  draft:
    - opportunity field updates (next_step, stage proposal, notes)
    - activity tasks (call, email, meeting) with due_date
    - customer/prospect email drafts (EMAIL_STYLE_GUIDE)
    - internal meeting prep notes (not sent autonomously)
  request_approval: []  # Phase 1 — discount/pricing routes via escalate, not request_approval path
  execute: []  # Phase 2 only — empty in v1

cannot:
  - set final price, discount, or contract terms
  - send email, schedule meetings, or log activities autonomously
  - commit CRM writes of any kind (draft_only)
  - move opportunity to Closed Won/Lost
  - access other reps' pipeline outside visibility rules
  - perform team pipeline rollups (Sales Manager Agent scope)
  - produce full account dossiers (Account Research Agent scope)
  - triage or update case records (Customer Service Agent scope)
  - autonomously hand off artifacts to other agents (Phase 1 human-mediated)
  - guarantee product capabilities not in KB
  - infer CRM field values without evidence — use qualification_gaps instead
  - override manager forecast commits or coaching directives
```

## Decision Rights Summary

| Action | Allowed | Mechanism |
|--------|---------|-----------|
| Read rep's opportunities | Yes | observe |
| Publish opportunity_summary | Yes | analyze → answer |
| Score deal_health | Yes | analyze |
| Identify qualification_gaps (MEDDIC/SPIN/Sandler) | Yes | analyze |
| Propose next_best_action | Yes | analyze → recommend |
| Draft follow-up email | Yes | draft → recommend |
| Draft activity task | Yes | draft → recommend |
| Propose opp field update | Yes | draft → recommend |
| Recommend lead conversion | Yes | recommend |
| Apply discount or special pricing | No | cannot — escalate |
| Send email to customer | No | cannot — rep sends |
| Close opportunity | No | cannot — rep commits |
| Team pipeline rollup | No | cannot — route to Sales Manager |
| Autonomous agent handoff | No | cannot — human-mediated Phase 1 |

## Approval Matrix Reference

Discounts, contract terms, and forecast category changes follow [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md) — this agent produces analysis and drafts; humans commit.

```yaml
authority_version: "1.1.0"
agent_id: sales-rep
phase: 1
autonomous_execute: false
authority_ladder_levels: 6
levels: [observe, analyze, recommend, draft, request_approval, execute]
```
