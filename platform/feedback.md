# Feedback Engine

Closes the loop between user actions and agent METRICS.md.

## Events

| Event | Metric Impact |
|-------|----------------|
| User accepts recommendation | ↑ acceptance rate |
| User edits draft | ↑ edit rate; training signal |
| User rejects / escalates | ↑ escalation rate |
| User re-asks same question | ↓ quality signal |

## Storage

Planned: `feedback` schema in [database.md](database.md)

## Usage

- Agent improvement prioritization (not auto fine-tune in v1)
- Manager dashboards
- QUALITY.md eval harness inputs

## TBD

- Feedback API contract
- Anonymization for aggregate reporting
