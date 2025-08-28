# Data Retention Policy (Ethical Research Edition)

Principles:
- Data minimization and short retention windows
- Clear, documented retention periods by data type
- Automatic deletion after retention period
- Immediate deletion on consent revocation or DSR request

Defaults (can be tightened per study):
- Keystroke metadata: 14 days
- Clipboard entries: 7 days
- Aggregated telemetry/metrics: 30 days

Implementation guidance:
- Store `created_at`/`expires_at` on records; scheduled job to purge expired
- Ensure backups follow the same retention windows
- Document exceptions (legal hold) and approval workflow
