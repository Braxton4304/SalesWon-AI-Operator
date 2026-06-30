# Tools

Phase 1 tool surface (SDK implementation pending). All tools respect ServiceNow ACL for authenticated user.

## query_case

**Purpose:** Retrieve case by number or sys_id with work notes, SLA, assignment, impact, urgency.

**When:** Any case-specific question.

**Parameters:** `case_number` or `sys_id`, `include_work_notes` (bool), `include_sla` (bool)

**Returns:** Case object per DATA_DICTIONARY required fields + optional priority, impact, urgency, account, contact.

## query_account_cases

**Purpose:** List open/recent cases for an account.

**When:** Account-level service history requests.

**Parameters:** `account_sys_id` or `account_name`, `state_filter`, `limit`

**Returns:** Case list with priority, state, severity-relevant fields for account triage.

## query_contact

**Purpose:** Retrieve contact and linked cases.

**When:** Identifying requester or communication target.

**Parameters:** `contact_sys_id` or `email`

## query_account

**Purpose:** Retrieve account tier, strategic flag, open case count.

**When:** Account strategic tier factor in DECISION_MODEL; VIP escalation checks.

**Parameters:** `account_sys_id` or `account_name`

## retrieve_knowledge

**Purpose:** Search customer KB / shared procedures for resolution steps.

**When:** User asks "how do we handle…" or agent detects known-issue pattern.

**Rule:** KB supplements case data; never replaces case state facts.

## draft_case_update

**Purpose:** Propose case comment, work note, state change, or customer email.

**When:** User requests draft or agent recommends communication.

**Parameters:** `case_sys_id`, `draft_type` (email | work_note | state_change), `payload`

**Returns:** Draft text for OUTPUT_SCHEMA `recommended_action.draft_payload` — **never commits**.

## draft_activity

**Purpose:** Propose follow-up task (callback, research).

**Parameters:** `related_case_sys_id`, `type`, `due_date`, `description`

## escalate_case

**Purpose:** Route to human with escalation payload per ESCALATION.md.

**Parameters:** `case_sys_id`, `reason`, `suggested_assignee_group`

## Tool Rules

1. `query_case` before any case assertion
2. No tool may set `commit: true` in Phase 1
3. Log correlation_id on every call for audit
4. `query_account` when account tier affects severity or escalation_required
5. KB retrieval does not substitute for missing required case fields — escalate per data-spec

```yaml
tools_version: "1.0.0"
agent_id: customer-service
primary_tools: [query_case, draft_case_update, escalate_case]
commit_enabled: false
```
