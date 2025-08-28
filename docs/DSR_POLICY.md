# Data Subject Requests (DSR) Policy (Ethical Research Edition)

Supported requests (where applicable):
- Access: provide subject with a summary and export of their data
- Deletion: delete subject data across primary storage and backups (when feasible)
- Rectification: update metadata upon verified request
- Consent revocation: stop processing and delete data collected under that consent

Process:
- Verify identity (multi-factor where possible)
- Record request with ticket ID and timestamp
- Fulfill within defined SLA (e.g., 30 days) and notify subject

Implementation guidance:
- Provide API endpoints/hooks for export/delete
- Ensure audit logs capture requests and outcomes
- Coordinate with retention jobs to prevent re-ingestion after deletion
