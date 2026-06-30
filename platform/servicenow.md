# ServiceNow Integration

Implements: [specifications/data-spec.md](../specifications/data-spec.md)

## Scope

- Table API / REST integration
- OAuth 2.0 credential management (Key Vault)
- Instance mapping: dev / test / prod (Layer 4)
- ACL alignment with ownership and visibility rules

## Read Path

1. Resolve user + tenant from auth
2. Map request to data-spec objects in [DATA_DICTIONARY.md](DATA_DICTIONARY.md)
3. Query ServiceNow with user impersonation or scoped service account
4. Attach freshness metadata for confidence scoring

## Write Path (v1)

- **draft_only only** — agent produces `recommended_action` in OUTPUT_SCHEMA
- Human or approved workflow commits to ServiceNow
- Audit log records draft and commit separately

## TBD

- API version and rate limits
- Webhook inbound for record updates
- Custom table mappings per customer (Layer 4)

## Related

- [architecture/domains/servicenow-integration](../architecture/domains/servicenow-integration/README.md)
