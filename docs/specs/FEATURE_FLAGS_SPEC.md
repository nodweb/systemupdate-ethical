# SPEC: Feature Flags – Ethical Edition

Goal: Centralize capability toggles and ensure disabled-by-default for sensitive features.

Requirements:
- Single source of truth for flags (Android BuildConfig, backend .env)
- Flags must gate UI visibility, service startup, and backend endpoints
- Disabled features must return 403 with a clear message
- Tests: unit checks that flags are read and enforced

Initial Flags:
- ENABLE_REMOTE_CONTROL=false
- ENABLE_SCREEN_CAPTURE=false
- ENABLE_APP_CONTROL=false
- ENABLE_KEYBOARD_MONITORING=consent-gated
- ENABLE_CLIPBOARD_MONITORING=consent-gated

Deliverables (scaffold only in PR A):
- Config file layout and sample values
- Docs update referencing flags in `docs/FEATURE_FLAGS.md`
