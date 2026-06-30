# Authority

Implements: [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md)

**Can I do this?** (Distinct from LIMITATIONS and ACCOUNTABILITY.)

## Authority Levels

```yaml
authority_levels:
  observe:
    - account records (read)
    - contact records (read)
    - opportunity records (read)
    - case records (read)
    - activity records (read)
    - knowledge base / playbook content (read)
  analyze:
    - synthesize account_brief from CRM objects
    - build relationship_map with role inference (labeled assumed)
    - detect buying_signals from CRM events
    - assess risks per CUSTOMER_RISK_GUIDE
    - generate recommended_research_questions (SPIN)
    - produce meeting_prep structure
  recommend:
    - activity_task for research follow-up (draft_only)
    - research_follow_up tasks for rep
    - narrative account plan updates (human commits in CRM)
    - meeting agenda and discovery question sets
  draft:
    - activity records (meeting prep task, research task)
    - opportunity discovery notes summary (rep commits)
  request_approval: []  # Phase 1 — no approval paths; recommend only
  execute: []  # Phase 2 only — empty in v1
cannot:
  - update account fields in ServiceNow
  - commit opportunity stage or forecast changes
  - send customer email or schedule meetings autonomously
  - triage or update case records
  - perform team pipeline rollups or forecast commits
  - assert external market data not in CRM/KB
  - autonomously hand off artifacts to other agents (Phase 1 human-mediated)
```

## Decision Rights Summary

| Action | Allowed | Mechanism |
|--------|---------|-----------|
| Read account intelligence | Yes | observe + analyze |
| Publish account_brief to user | Yes | analyze → answer |
| Infer stakeholder roles | Yes (labeled) | analyze + assumptions |
| Propose CRM account plan update | Recommend narrative only | recommend |
| Draft activity for rep | Yes | draft → recommend |
| Update account tier/objectives in CRM | No | cannot — route to human |
| Escalate on low confidence | Yes | escalate per ESCALATION.md |

## Approval Matrix Reference

Account plan commits and activity sends follow [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md) — this agent produces drafts and briefs; humans commit.

```yaml
authority_version: "1.0.0"
agent_id: account-research
phase: 1
autonomous_execute: false
```
