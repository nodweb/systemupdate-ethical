import os
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token


dev_bp = Blueprint("dev", __name__)


def _enabled() -> bool:
    return os.getenv("DEV_JWT_ENABLED", "false").lower() in ("1", "true", "yes")


def _secret_ok(req) -> bool:
    expected = os.getenv("DEV_JWT_SECRET")
    if not expected:
        return False
    provided = req.headers.get("X-Dev-Secret")
    return provided is not None and provided == expected


@dev_bp.post("/mint_jwt")
def mint_jwt():
    if not _enabled():
        return jsonify(error="disabled"), 404
    if not _secret_ok(request):
        return jsonify(error="unauthorized"), 401

    body = request.get_json(silent=True) or {}
    device_id = body.get("device_id") or "dev-device"
    consent = bool(body.get("consent", True))
    claims = {"consent": consent, "device_id": device_id}
    token = create_access_token(identity=device_id, additional_claims=claims)
    return jsonify(token=token, claims=claims), 200
