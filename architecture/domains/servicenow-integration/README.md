# ServiceNow Integration

## Scope

- Table API / REST integration patterns
- OAuth and credential management
- Instance mapping (dev/test/prod)
- ACL alignment with data-spec ownership rules

## Key Questions

- Which ServiceNow products: CSM, Sales & Order Management, custom apps?
- Inbound vs. outbound integration (webhooks, scheduled sync)?
- How draft-only writes become ServiceNow records?

## Related

- [specifications/data-spec.md](../../specifications/data-spec.md)
- [platform/servicenow.md](../../platform/servicenow.md)
- [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md)

## Decisions Pending

- ServiceNow API version and rate limits
- Write workflow (approval queue vs. direct draft table)
