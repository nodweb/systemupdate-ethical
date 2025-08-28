# SPEC: Monitoring – Keyboard & Clipboard (Ethical Edition)

Goal: Capture keystroke metadata via AccessibilityService and clipboard text with explicit consent, redaction, and per-app exclusions.

Keyboard Monitoring (Accessibility):
- Events: key down/up, focused app/package, timestamp
- Do not capture password fields (TYPE_TEXT_VARIATION_PASSWORD etc.)
- Respect per-app exclude list (package names)
- Buffer locally; backoff + retry on upload failures

Clipboard Monitoring:
- Listen for primary clip changes; capture text, source app, timestamp
- Redact sensitive patterns (OTP, card, IBAN) before storage/upload
- Respect per-app excludes

Upload Strategy:
- Batch size limits (e.g., <=500), max payload size
- Exponential backoff with jitter; drop oldest beyond retention window

Consent Gating:
- Both features disabled until consent granted and system settings enabled
- Surface Pause/Stop toggle and per-feature enablement in UI

Telemetry:
- Minimal metrics: counts and last upload timestamps (no raw data)
