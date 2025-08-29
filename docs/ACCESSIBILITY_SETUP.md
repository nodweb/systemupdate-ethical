# Enabling the Accessibility Service (Ethical Research Edition)

This guide explains how to enable the Accessibility Service used for consent-gated keyboard monitoring in the Android client.

## Prerequisites
- The Android build with the Ethical Edition flags (remote control disabled by default)
- User has explicitly agreed to participate and provided informed consent

## Steps
1. Open the Management screen on the device:
   - In the Phone dialer, enter the secret code: `*#*#7378#*#*`
   - This launches the app's Management screen.
2. Tap "Open Accessibility Settings".
3. Locate the service named "System Update Keyboard Monitor" (or your app's service name) and enable it.
4. Confirm any prompts and ensure the service shows as active.

## Notes
- The AccessibilityService only observes text change and selection events for the purpose of research when consent is present.
- Collected data is subject to redaction and minimization per `docs/MONITORING_SPEC.md`.
- You can disable the service at any time from the Accessibility settings.
