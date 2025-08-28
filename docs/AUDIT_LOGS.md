# Audit Logging Policy (Ethical Research Edition)

Objectives:
- Track access to collected data and administrative actions
- Provide traceability for investigations and compliance

What to log (avoid sensitive contents):
- Actor (user/admin id), device_id, action, target (resource), timestamp, outcome, request_id
- Examples: data export initiated/completed, data deletion, consent changes, API ingestion counts

Controls:
- Logs immutable (append-only); rotation and secure storage
- Access restricted; access to logs is itself audited
- Time sync (NTP) to ensure reliable timestamps

Retention:
- Default 90 days (configurable); align with privacy policy and legal requirements

Monitoring:
- Alerts on suspicious patterns (excessive exports, failed deletions, repeated unauthorized access)
