# Android Scaffold (Ethical Research Edition)

Purpose:
- Establish a minimal module to host feature flags and consent-aware UI stubs.

Next steps:
- Create a `featureflags` package with default-off flags (remote control disabled).
- Add a `consent` package with stub activities/dialogs following `docs/specs/CONSENT_UI_SPEC.md`.
- No permissions requested until consent is granted (see `docs/CONSENT.md`).
- Avoid collecting any data until explicit consent flow completes.
