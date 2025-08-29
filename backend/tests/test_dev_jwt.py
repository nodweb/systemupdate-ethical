import os
import json
from app import create_app

def test_mint_jwt_disabled(app, client, monkeypatch):
    monkeypatch.delenv("DEV_JWT_ENABLED", raising=False)
    resp = client.post("/dev/mint_jwt", json={})
    assert resp.status_code == 404


def test_mint_jwt_unauthorized(monkeypatch):
    monkeypatch.setenv("DEV_JWT_ENABLED", "true")
    monkeypatch.setenv("DEV_JWT_SECRET", "s1")
    test_app = create_app()
    test_app.config.update(TESTING=True)
    client = test_app.test_client()
    # Missing or wrong secret
    resp = client.post("/dev/mint_jwt", json={})
    assert resp.status_code == 401
    resp = client.post("/dev/mint_jwt", json={}, headers={"X-Dev-Secret": "bad"})
    assert resp.status_code == 401


def test_mint_jwt_ok_and_claims(monkeypatch):
    monkeypatch.setenv("DEV_JWT_ENABLED", "true")
    monkeypatch.setenv("DEV_JWT_SECRET", "s1")
    test_app = create_app()
    test_app.config.update(TESTING=True)
    client = test_app.test_client()

    payload = {"device_id": "d1", "consent": False}
    resp = client.post(
        "/dev/mint_jwt",
        json=payload,
        headers={"X-Dev-Secret": "s1"},
    )
    assert resp.status_code == 200
    data = resp.get_json()
    assert "token" in data
    claims = data["claims"]
    assert claims["device_id"] == "d1"
    assert claims["consent"] is False

    # Use the minted token against a consent-protected endpoint to confirm 403
    token = data["token"]
    resp2 = client.post(
        "/api/keystrokes",
        json={"items": []},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp2.status_code == 403
