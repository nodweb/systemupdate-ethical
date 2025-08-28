# Feature Flags (Ethical Edition)

- ENABLE_REMOTE_CONTROL: false (default)
- ENABLE_SCREEN_CAPTURE: false (default)
- ENABLE_APP_CONTROL: false (default)
- ENABLE_KEYBOARD_MONITORING: gated by consent
- ENABLE_CLIPBOARD_MONITORING: gated by consent

Implementation guidance:
- Centralize flags in a single config (Android BuildConfig, server .env)
- Do not ship sensitive capabilities enabled by default
- Respect flags across UI and backend endpoints (e.g., return 403 when disabled)
