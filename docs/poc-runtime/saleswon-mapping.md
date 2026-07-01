# ServiceNow Mapping Config

Implements: [data-spec](../../specifications/data-spec.md), [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md)

## File

[`apps/poc-runtime/backend/config/saleswon_mapping.yaml`](../../apps/poc-runtime/backend/config/saleswon_mapping.yaml)

## Purpose

Maps SalesWon business objects to ServiceNow tables and fields before credentials arrive. Values are `TODO_*` placeholders until SalesWon provides real table/field names.

## When credentials arrive

1. Replace `TODO_opportunity_table`, `TODO_activity_table`, etc. with real ServiceNow table names
2. Replace field mappings with actual column names from your instance
3. Set `SERVICENOW_*` env vars in `.env`
4. No code changes required — connector reads mapping at runtime

## Used by

- `ServiceNowSalesWonConnector` — table names for API calls
- `PromptCompiler` — CRM schema summary for LLM grounding
- `PlanExecutor` — filter translation (future)

## Example entry

```yaml
objects:
  activity:
    table: task
    fields:
      status: state
      due_date: due_date
```
