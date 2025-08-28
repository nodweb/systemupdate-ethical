# SPEC: Consent UI – Ethical Edition

Goal: Ensure explicit, informed consent before enabling any monitoring features.

Flow:
1. Welcome screen: purpose, scope, and plain-language summary
2. Details screen: data categories, retention, risks, opt-out
3. Review & Accept: checkbox + "I Agree" (disabled until scrolled/read)
4. System intents: navigate to Accessibility (and optional Usage Access)
5. Post-consent: enable feature flags gated by consent; show pause/stop controls

Requirements:
- Consent is versioned and timestamped; stored locally and optionally sent to backend during device registration
- Per-feature toggles (keyboard/clipboard) must remain disabled without consent
- Provide per-app exclusion UI for keyboard monitoring
- Export/Delete: allow user to view and revoke consent, export gathered data, and request deletion

Deliverables (scaffold in PR A):
- Wireframe placeholders (images/txt references)
- Consent text template referencing `docs/CONSENT.md`
- Data model sketch for local consent record
- Update CI to ensure consent docs exist (already covered)
