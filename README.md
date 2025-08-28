# SystemUpdate – Ethical Research Edition

Status: Planning and scaffolding phase.

This repository houses the ethical, consent-first variant of SystemUpdate designed for educational and controlled research environments.

![CI](https://github.com/nodweb/systemupdate-ethical/actions/workflows/ci.yml/badge.svg)

Key principles:
- Explicit, informed user consent
- Transparency and data minimization
- Feature flags (remote control disabled by default)
- Clipboard/keyboard monitoring only with consent and redaction

See `docs/ETHICAL_RESEARCH_MOD_PLAN.md` for the full implementation plan and acceptance criteria.

## Governance

- **Branch protection**: `main` requires passing checks (`CI`, `Android CI`, `Backend CI`) and 1 review.
- **Merging**: squash merges only to keep history clean.
- **CODEOWNERS**: see `.github/CODEOWNERS` for default reviewers.
- **Releases**: tags with annotated notes; docs-only `v0.1.0` published.
- **Compliance**: follow `docs/PRIVACY.md`, `docs/CONSENT.md`, `docs/SECURITY.md`, `docs/RETENTION_POLICY.md`, `docs/AUDIT_LOGS.md`, `docs/DSR_POLICY.md`.
