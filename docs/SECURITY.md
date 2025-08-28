# Security Guidelines (Ethical Research Edition)

- Transport: Enforce TLS; validate server certificates. Consider certificate pinning for mobile.
- Authentication: JWT with device binding (device_id claim), short expirations, refresh rotation.
- Authorization: Feature-flag checks on all sensitive endpoints. Disabled features must return 403.
- Crypto: Encrypt payloads client-side where feasible. Encrypt sensitive fields at rest (DB/field-level).
- Storage: Apply least privilege for DB users; backups encrypted; retention windows short and documented.
- Logging: Avoid sensitive data in logs. Maintain audit logs for access to collected data.
- Secrets: Use environment variables or secret manager; never commit secrets.
- Threats: MITM, token theft, replay attacks (use nonce/timestamps), endpoint enumeration (rate-limit & WAF), device impersonation (key pairs, attestations when feasible).
- Compliance: Honor consent; provide export/delete flows. Document data flows and DPIA where applicable.
