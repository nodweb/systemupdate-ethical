import json
from flask_jwt_extended import create_access_token


def make_token(app, consent=True, device_id="test-device"):
    with app.app_context():
        return create_access_token(identity=device_id, additional_claims={
            "consent": bool(consent),
            "device_id": device_id,
        })


def test_keystrokes_requires_consent(app, client):
    token = make_token(app, consent=False)
    resp = client.post(
        "/api/keystrokes",
        json={"items": [{"timestamp": 1, "package": "p", "text": "t", "eventType": "e"}]},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 403
    data = resp.get_json()
    assert data["error"] == "consent_required"


def test_keystrokes_emails_ok(app, client, monkeypatch):
    sent = {}

    def fake_send(subject, body):
        sent["subject"] = subject
        sent["body"] = body
        return None  # no error

    monkeypatch.setenv("EMAIL_REPORT_TO", "audit@example.com")
    monkeypatch.setattr("app.emailer.send_email_report", fake_send)

    token = make_token(app, consent=True, device_id="dev1")
    payload = {"items": [
        {"timestamp": 1, "package": "pkg", "text": "hello", "eventType": "text_changed"},
        {"timestamp": 2, "package": "pkg", "text": "world", "eventType": "text_changed"},
    ]}
    resp = client.post(
        "/api/keystrokes",
        json=payload,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 202
    data = resp.get_json()
    assert data["status"] == "emailed"
    assert data["count"] == 2
    assert "Keystrokes from dev1" in sent["subject"]
    body_json = json.loads(sent["body"])  # should be JSON-serialised
    assert len(body_json.get("items", [])) == 2


def test_clipboard_emails_ok(app, client, monkeypatch):
    sent = {}

    def fake_send(subject, body):
        sent["subject"] = subject
        sent["body"] = body
        return None

    monkeypatch.setenv("EMAIL_REPORT_TO", "audit@example.com")
    monkeypatch.setattr("app.emailer.send_email_report", fake_send)

    token = make_token(app, consent=True, device_id="dev2")
    payload = {"text": "copied text"}
    resp = client.post(
        "/api/clipboard",
        json=payload,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 202
    data = resp.get_json()
    assert data["status"] == "emailed"
    assert data["length"] == len("copied text")
    assert "Clipboard from dev2" in sent["subject"]


def test_clipboard_email_error(app, client, monkeypatch):
    def boom(subject, body):
        raise RuntimeError("smtp down")

    monkeypatch.setenv("EMAIL_REPORT_TO", "audit@example.com")
    monkeypatch.setattr("app.emailer.send_email_report", boom)

    token = make_token(app, consent=True)
    resp = client.post(
        "/api/clipboard",
        json={"text": "x"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 202
    data = resp.get_json()
    assert data["status"].startswith("email_error:")
