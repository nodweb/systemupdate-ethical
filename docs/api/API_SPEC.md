# API SPEC – Ethical Research Edition (PR B)

## Overview
Adds consent-aware data ingestion endpoints and disables remote-control features.

## Global Requirements
- All endpoints require HTTPS and JWT auth (Bearer).
- Include `X-Device-Id` header bound to token subject.
- If feature is disabled by flag, return `403 {"error":"feature_disabled"}`.

## Endpoints

### POST /api/data/keystrokes
- Purpose: Upload buffered keystroke events.
- Auth: Bearer JWT (device-bound)
- Request headers:
  - Content-Type: application/json
  - X-Device-Id: <uuid>
- Request body (encrypted field optional):
```json
{
  "consent_version": "1.0.0",
  "events": [
    {
      "t": 1725148800,
      "app": "com.example.app",
      "key": "a",
      "type": "down|up",
      "redacted": false
    }
  ],
  "encryption": {
    "alg": "AES-GCM",
    "kid": "device-key-1"
  }
}
```
- Responses:
  - 202 Accepted: {"accepted": true, "count": N}
  - 400 Bad Request: validation error
  - 401/403 Unauthorized/feature_disabled

### POST /api/data/clipboard
- Purpose: Upload clipboard texts with redaction.
- Auth: Bearer JWT (device-bound)
- Request headers:
  - Content-Type: application/json
  - X-Device-Id: <uuid>
- Request body:
```json
{
  "consent_version": "1.0.0",
  "entries": [
    {
      "t": 1725148800,
      "text": "copied content (may be redacted)",
      "source_app": "com.example.app",
      "redacted": true
    }
  ]
}
```
- Responses: same pattern as keystrokes

## Remote Control Endpoints
- All remote-control routes and socket events return 403 when flags disabled.

## Validation
- consent_version required and must match server-supported versions
- events/entries array size limits (e.g., <= 1000) and payload size caps
- rate limiting per device

## Telemetry & Audit
- Store minimal metadata (counts, timestamps) for monitoring
- Audit log entries for each ingestion with device_id and count
