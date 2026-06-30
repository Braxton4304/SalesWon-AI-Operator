# Escalation

Role-specific escalation rules. Mandatory triggers from [shared/escalation-framework.md](../../shared/escalation-framework.md) always apply.

## Mandatory Escalation (This Agent)

| Condition | Route To |
|-----------|----------|
| Confidence < 0.60 after retrieval | *(Role — e.g. Team Lead)* |
| Legal or compliance keyword detected | *(Legal contact — Layer 4)* |
| User says "speak to a human" | Next available agent |
| Write blocked by data-spec | Human with write access |

## Optional Escalation

| Condition | Route To |
|-----------|----------|
| Sentiment severely negative | Senior CS rep |
| Strategic account flag | Account executive |

## Escalation Payload

Include per escalation-framework: request, attempted actions, confidence, sources, suggested assignee.

## Layer 4 Configuration

Customer-specific contacts and ServiceNow assignment groups — not in this repo.
