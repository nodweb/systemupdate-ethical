# Backend Scaffold (Ethical Research Edition)

Purpose:
- Provide a placeholder service boundary for consent-aware ingestion and DSR endpoints.

Next steps:
- Define a minimal Flask/FastAPI skeleton (private repo) with JWT auth and device-bound claims.
- Implement stub endpoints gated by feature flags per `docs/api/API_SPEC.md`.
- Add retention purge job (no-op placeholder) aligned with `docs/RETENTION_POLICY.md`.
- Add audit logging hooks aligned with `docs/AUDIT_LOGS.md`.
- Do not accept or store any PII until explicit consent is recorded.
