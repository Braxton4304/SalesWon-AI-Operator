# Data Dictionary

Implements: [specifications/data-spec.md](../specifications/data-spec.md)

Maps ServiceNow tables to business meaning, AI usage, confidence, and write permissions.

## Entry Format

Each object follows the data-spec field contract:

```yaml
object: {name}
purpose: {business meaning}
readable: true|false
writable: none|draft_only|full
confidence: high|medium|low|field_dependent
required_fields: []
optional_fields: []
source_of_truth: servicenow
missing_data_behavior: ask|retrieve|escalate|refuse
ownership_rule: record_owner|team|role_based
visibility_rule: tenant_scope
```

---

## Opportunity

```yaml
object: opportunity
purpose: Sales pipeline tracking and forecast
readable: true
writable: draft_only
confidence: high
required_fields:
  - amount
  - probability
  - close_date
  - owner
optional_fields:
  - stage
  - description
  - next_step
  - account
source_of_truth: servicenow
missing_data_behavior: ask
ownership_rule: record_owner
visibility_rule: tenant_scope
```

**AI usage:** Pipeline health, activity prioritization, forecast summaries, next-best-action recommendations.

**Write permissions:** Agent may propose stage updates, next_step, activity drafts — human or workflow commits.

---

## Account

```yaml
object: account
purpose: Customer organization master record
readable: true
writable: none
confidence: high
required_fields:
  - name
optional_fields:
  - industry
  - tier
  - parent_account
source_of_truth: servicenow
missing_data_behavior: retrieve
ownership_rule: record_owner
visibility_rule: tenant_scope
```

**AI usage:** Context for opportunities, cases, and communications. No direct writes in v1.

---

## Contact

```yaml
object: contact
purpose: People associated with accounts
readable: true
writable: none
confidence: high
required_fields:
  - name
optional_fields:
  - email
  - phone
  - title
  - account
source_of_truth: servicenow
missing_data_behavior: ask
ownership_rule: record_owner
visibility_rule: tenant_scope
```

**AI usage:** Identify stakeholders, threading, communication targets. Draft contact updates via recommend only if Layer 4 enables.

---

## Case

```yaml
object: case
purpose: Customer service incidents and requests
readable: true
writable: draft_only
confidence: high
required_fields:
  - short_description
  - state
  - assigned_to
optional_fields:
  - priority
  - account
  - contact
  - resolution_notes
source_of_truth: servicenow
missing_data_behavior: escalate
ownership_rule: team
visibility_rule: tenant_scope
```

**AI usage:** Case triage, status summaries, draft responses, SLA monitoring.

**Write permissions:** Draft comments and state change proposals — not direct close without approval.

---

## Activity

```yaml
object: activity
purpose: Tasks, calls, meetings, emails
readable: true
writable: draft_only
confidence: medium
required_fields:
  - type
  - due_date
optional_fields:
  - related_opportunity
  - related_account
  - description
source_of_truth: servicenow
missing_data_behavior: ask
ownership_rule: record_owner
visibility_rule: tenant_scope
```

**AI usage:** Activity prioritization, follow-up recommendations, calendar-aware suggestions.

---

## Lead

```yaml
object: lead
purpose: Pre-qualification pipeline
readable: true
writable: draft_only
confidence: medium
required_fields:
  - name
  - status
optional_fields:
  - company
  - source
  - rating
source_of_truth: servicenow
missing_data_behavior: ask
ownership_rule: record_owner
visibility_rule: tenant_scope
```

**AI usage:** Qualification scoring, conversion recommendations.

---

## Machine-Readable Index

```json
{
  "implements": "data-spec",
  "dictionary_version": "1.0.0",
  "objects": ["opportunity", "account", "contact", "case", "activity", "lead"]
}
```

## Extension

New CRM objects require data-spec update first, then entry here, then ADR in architecture/DECISIONS.md.
