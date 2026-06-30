# Output Schema

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

Every response MUST validate against this schema.

## Machine-Readable Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "FollowUpAgentOutput",
  "type": "object",
  "required": [
    "summary",
    "confidence",
    "sources",
    "decision_action",
    "follow_up_priority",
    "reason",
    "recommended_timing",
    "suggested_message",
    "escalation_required",
    "missing_data",
    "source_records"
  ],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Human-readable follow-up recommendation summary"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "sources": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "id"],
        "properties": {
          "type": { "enum": ["crm", "kb", "policy"] },
          "id": { "type": "string" },
          "label": { "type": "string" }
        }
      }
    },
    "decision_action": {
      "enum": ["answer", "ask", "retrieve", "escalate", "refuse", "recommend"]
    },
    "follow_up_priority": {
      "enum": ["critical", "high", "moderate", "low"]
    },
    "reason": {
      "type": "string",
      "description": "CRM-grounded rationale for priority and timing"
    },
    "recommended_timing": {
      "type": "string",
      "description": "When to execute the follow-up (specific window)"
    },
    "suggested_message": {
      "type": "string",
      "description": "Draft email body or call talking points"
    },
    "related_opportunity": {
      "type": ["object", "null"],
      "properties": {
        "id": { "type": "string" },
        "name": { "type": "string" },
        "stage": { "type": "string" },
        "close_date": { "type": "string", "format": "date" },
        "amount": { "type": "number" }
      }
    },
    "related_activity": {
      "type": ["object", "null"],
      "properties": {
        "id": { "type": "string" },
        "type": { "type": "string" },
        "due_date": { "type": "string", "format": "date" },
        "days_overdue": { "type": "integer" },
        "state": { "type": "string" }
      }
    },
    "escalation_required": {
      "type": "boolean"
    },
    "missing_data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "field": { "type": "string" },
          "object": { "enum": ["activity", "opportunity", "contact", "account"] },
          "impact": { "type": "string" }
        }
      }
    },
    "source_records": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "id"],
        "properties": {
          "type": { "enum": ["activity", "opportunity", "account", "contact", "kb"] },
          "id": { "type": "string" },
          "label": { "type": "string" }
        }
      }
    },
    "recommended_action": {
      "type": "object",
      "description": "Required when decision_action is recommend",
      "properties": {
        "type": { "enum": ["email_draft", "activity_task", "escalation"] },
        "target_record_id": { "type": "string" },
        "draft_payload": {
          "type": "object",
          "properties": {
            "subject": { "type": "string" },
            "body": { "type": "string" },
            "proposed_due_date": { "type": "string", "format": "date" },
            "activity_type": { "type": "string" }
          }
        }
      }
    },
    "clarifying_question": {
      "type": "string",
      "description": "Required when decision_action is ask"
    }
  }
}
```

## Example — Overdue Activity with Email Draft

```json
{
  "summary": "Critical: Call task 5 days overdue on Acme Expansion ($120K, closes in 11 days). Send re-engagement email today.",
  "confidence": 0.92,
  "sources": [
    { "type": "crm", "id": "act456", "label": "Follow-up call - Acme" },
    { "type": "crm", "id": "opp789", "label": "Acme Expansion FY26" }
  ],
  "decision_action": "recommend",
  "follow_up_priority": "critical",
  "reason": "Activity due 2026-06-25 is 5 days overdue; linked opp closes 2026-07-11 with no completed activity in 19 days.",
  "recommended_timing": "Today by 5:00 PM ET",
  "suggested_message": "Hi Sarah,\n\nThank you again for the time on our demo last week. I wanted to follow up on the integration timeline we discussed and confirm whether Tuesday works for a quick call with your IT lead.\n\nWould 2 PM ET Tuesday work on your end?\n\nBest regards,",
  "related_opportunity": {
    "id": "opp789",
    "name": "Acme Expansion FY26",
    "stage": "Proposal",
    "close_date": "2026-07-11",
    "amount": 120000
  },
  "related_activity": {
    "id": "act456",
    "type": "Call",
    "due_date": "2026-06-25",
    "days_overdue": 5,
    "state": "Open"
  },
  "escalation_required": false,
  "missing_data": [],
  "source_records": [
    { "type": "activity", "id": "act456", "label": "Follow-up call - Acme" },
    { "type": "opportunity", "id": "opp789", "label": "Acme Expansion FY26" },
    { "type": "contact", "id": "con112", "label": "Sarah Chen" }
  ],
  "recommended_action": {
    "type": "email_draft",
    "target_record_id": "act456",
    "draft_payload": {
      "subject": "Acme Expansion — next steps on integration timeline",
      "body": "Hi Sarah,\n\nThank you again for the time on our demo last week..."
    }
  }
}
```

## Example — Objection with Escalation

```json
{
  "summary": "High priority re-engagement for Globex opp; customer cited pricing objection — escalate before offering discount.",
  "confidence": 0.78,
  "sources": [{ "type": "crm", "id": "opp321", "label": "Globex Platform Renewal" }],
  "decision_action": "escalate",
  "follow_up_priority": "high",
  "reason": "Last call note: 'price too high'; opp at Proposal stage, close in 22 days, 12 days since last activity.",
  "recommended_timing": "Within 2 business days after manager alignment on value narrative",
  "suggested_message": "Hi Marcus,\n\nI appreciate your candor on budget. Before we discuss numbers, I'd like to recap the ROI targets your team shared in our last session — specifically the 18% reduction in manual processing you modeled.\n\nCould we schedule 20 minutes to validate those assumptions together?",
  "related_opportunity": {
    "id": "opp321",
    "name": "Globex Platform Renewal",
    "stage": "Proposal",
    "close_date": "2026-07-22",
    "amount": 85000
  },
  "related_activity": null,
  "escalation_required": true,
  "missing_data": [
    { "field": "economic_buyer", "object": "opportunity", "impact": "Reduced confidence on stakeholder targeting" }
  ],
  "source_records": [
    { "type": "opportunity", "id": "opp321", "label": "Globex Platform Renewal" },
    { "type": "activity", "id": "act998", "label": "Discovery call - Globex" }
  ]
}
```
