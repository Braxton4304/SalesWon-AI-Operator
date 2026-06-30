# Reasoning Patterns

Agent-specific reasoning chains. Maps to [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) actions.

## Pattern 1: Full Account Brief

```text
Input (account name/ID)
  → Step 1: Resolve account (query_account) — ask if ambiguous
  → Step 2: Gather contacts (query_contacts) → relationship_map draft
  → Step 3: Gather opps (query_opportunities) → opportunity_context + buying_signals
  → Step 4: Gather cases (query_cases) → service_context + risks (CUSTOMER_RISK_GUIDE)
  → Step 5: Gather activities (query_activities) → engagement recency, meeting_prep data
  → Step 6: Apply ACCOUNT_PLANNING → snapshot + ninety_day_objectives
  → Step 7: Generate recommended_research_questions (DISCOVERY_PLAYBOOK / SPIN)
  → Step 8: Compute confidence → label missing_data and assumptions
  → Step 9: decision_action answer | escalate if confidence < threshold
```

## Pattern 2: Meeting Prep Overlay

```text
Input (account + meeting date + attendees)
  → Steps 1–5 from Pattern 1 (reuse short memory if fresh)
  → Step 6: Filter relationship_map to attendees; enrich engagement_summary
  → Step 7: Build recommended_agenda (MEETING_PREPARATION)
  → Step 8: Summarize last 5 activities
  → Step 9: Elevate risks if P1/P2 open → agenda includes resolution topic
  → Step 10: answer with account_brief.meeting_prep populated
```

## Pattern 3: Service Health Focus

```text
Input (account + service health request)
  → Step 1: query_account + query_cases (priority filter P1/P2)
  → Step 2: Assess sentiment from case notes (no fabrication)
  → Step 3: Cross-reference renewal/expansion opps (CUSTOMER_RISK_GUIDE)
  → Step 4: risks array with severity
  → Step 5: answer — other sections minimal but present
```

## Pattern 4: Relationship Map Only

```text
Input (account + stakeholder request)
  → Step 1: query_contacts + query_activities per contact
  → Step 2: Assign role_label with role_confidence
  → Step 3: Infer reporting lines only when CRM hierarchy exists
  → Step 4: assumptions for inferred roles
  → Step 5: answer — relationship_map primary; brief snapshot condensed
```

## Decision Engine Mapping

| Step Outcome | decision_action |
|--------------|-----------------|
| Account not found | ask or retrieve |
| Multiple account matches | ask |
| Required data missing after 3 retrieves | escalate |
| External intel requested | refuse |
| Research task appropriate | recommend (draft_activity) |
| Sufficient CRM context | answer |

```yaml
reasoning_version: "1.0.0"
agent_id: account-research
patterns: [full_brief, meeting_prep, service_health, relationship_map]
```
