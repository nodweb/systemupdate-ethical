# SYSTEMUPDATE PROJECT MODIFICATION - ETHICAL RESEARCH VERSION (Plan Only)

Status: Documentation-only plan. No code has been changed.

This document consolidates the requested ethical version changes into a clear, auditable plan while preserving existing architecture. It outlines what to disable, what to add, consent/UX, backend adjustments, testing, and rollout strategy.

---

## 1) Roles & Principles

- Senior Android Security Engineer
- Privacy & Ethics Compliance Officer
- Software Architect (Clean Architecture, Feature Flags)
- UX Security Specialist (Consent & Transparency)
- Backend Engineer (Secure APIs & Storage)

Ethical constraints (must): Educational, consent-based research, parental/corporate use with transparency. No malicious/unauthorized surveillance.

---

## 2) Execution Parameters

- MAINTAIN_ETHICS: true
- PRESERVE_ARCHITECTURE: true
- ADD_CONSENT_MECHANISMS: true
- IMPLEMENT_TRANSPARENTLY: true
- DOCUMENT_CHANGES: true

---

## 3) Android App Changes (Planned)

### 3.1 Disable Remote Control Features (via feature flags)

Feature flags (BuildConfig):
- ENABLE_REMOTE_CONTROL = false
- ENABLE_SCREEN_CAPTURE = false
- ENABLE_APP_CONTROL = false

Scope to gate behind flags (no removals yet):
- RemoteControlService
- ScreenCaptureService
- AppControlManager
- RemoteCommandExecutor

Notes:
- Keep code paths behind flags for reversible, testable toggles.
- Do not request sensitive permissions not used by the ethical build (e.g., SYSTEM_ALERT_WINDOW, CAPTURE_SECURE_VIDEO_OUTPUT, READ_SMS, etc.).

### 3.2 Replace Data Collection (SMS/File) with Keyboard/Clipboard Monitoring (Consent-based)

Remove collectors:
- SmsCollector, FileCollector (and their manifest permissions) – only in a future code change PR.

Add components (consent required):
- KeyboardMonitorService (AccessibilityService)
- ClipboardMonitorService (ClipboardManager listener)

Consent flow:
- ConsentActivity to present scope, purpose, data minimization, opt-out.
- Store signed consent (timestamp, version, scope) locally; send consent proof to backend with device registration.

Runtime activation (user-driven):
- Open Accessibility Settings via intent.
- (Optional) Usage Access intent for better context.

Privacy controls:
- Allow per-app exclude list.
- Redact sensitive fields (password inputs, OTP, card numbers where detectable).

### 3.3 App Visibility (Optional, transparent mode preferred)

- Prefer transparent mode (visible app with clear purpose and consent).
- If needed for lab-only experiments, hide launcher icon post-setup; still visible in Settings > Apps. Not uninstall-resistant.
- Do not implement Device Owner/Kiosk (requires provisioning/factory reset and is out of scope).

---

## 4) Backend Changes (Planned)

- Disable remote control endpoints and socket events (return 403 "Feature disabled").
- Add new endpoints:
  - POST /api/data/keystrokes (encrypted payload)
  - POST /api/data/clipboard (encrypted payload)
- Data model: KeystrokeData, ClipboardData with consent linkage (device_id, consent_version).
- Storage: apply retention policy; encrypted at rest (DB-level or application-level field encryption where feasible).
- Access control: JWT + device binding; audit logs.

---

## 5) Minimal Permissions & Settings

Manifest (install-time):
- Keep: INTERNET, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE, FOREGROUND_SERVICE_DATA_SYNC, RECEIVE_BOOT_COMPLETED
- Runtime (API 33+): POST_NOTIFICATIONS
- Remove if unused: READ_SMS, SEND_SMS, READ_CONTACTS, READ_PHONE_STATE, storage permissions, QUERY_ALL_PACKAGES

User activations (post-install, one-time):
- Enable Accessibility Service (for keyboard monitoring)
- (Optional) Enable Usage Access (context)

Optional (session-based):
- MediaProjection (screen sharing) – disabled by flag in ethical build

---

## 6) UX & Consent

- Consent screens with clear scope, data categories, retention, opt-out.
- In-app setup wizard to guide users to Accessibility/Usage settings.
- Provide pause/stop monitoring controls.
- Expose data access/export/delete per subject request (where applicable).

---

## 7) Security & Compliance

- TLS everywhere; server cert validation (pinning if feasible).
- Device authentication and key rotation.
- Data minimization and redaction rules.
- Audit logs for access to collected data.
- Retention and deletion policies documented and enforced.

---

## 8) Testing Plan

- Unit tests: consent gating, buffer & upload logic, redaction.
- Instrumented tests: Accessibility event handling (mock), clipboard listener.
- Backend tests: JWT, schema validation, decrypt & persist.
- E2E (lab): onboarding wizard, consent acceptance, settings activation, sample data flow.

---

## 9) Rollout Plan (No Code Changes Yet)

- Phase 1: Documentation & design sign-off (this document)
- Phase 2: Feature flag scaffolding + consent UI (PR A)
- Phase 3: Disable remote-control endpoints + new data endpoints (PR B)
- Phase 4: Keyboard/Clipboard monitoring implementation (PR C)
- Phase 5: Privacy redaction + retention + admin audit (PR D)

Each PR will include migration notes and updated docs.

---

## 10) Artifacts to Update in Future PRs

- Android: `AndroidManifest.xml`, feature flags in Gradle, new services & XML config
- Backend: routes, models, migrations, configs
- Docs: README, PRIVACY.md, CONSENT.md, API docs, onboarding guide

---

## 11) Out of Scope

- Device Owner/Kiosk provisioning
- OEM privileged plugins
- Hidden screen capture without consent

---

## 12) Acceptance Criteria (Ethical Version)

- Remote control disabled by flags and endpoints respond 403
- No sensitive unused permissions in manifest
- Consent flow required before any monitoring
- Accessibility-based keyboard monitoring works in lab tests, with redaction and opt-out
- Clipboard monitoring works with user control and opt-out
- Backend securely receives and stores encrypted data with audit logs
