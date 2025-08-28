from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt


data_bp = Blueprint("data", __name__)


# Simple consent check stub: require claim consent=true

def _has_consent() -> bool:
    claims = get_jwt() or {}
    return bool(claims.get("consent", False))


@data_bp.post("/keystrokes")
@jwt_required()
def post_keystrokes():
    if not _has_consent():
        return jsonify(error="consent_required"), 403
    payload = request.get_json(silent=True) or {}
    # TODO: decrypt, redact, persist
    return jsonify(status="accepted", count=len(payload.get("items", []))), 202


@data_bp.post("/clipboard")
@jwt_required()
def post_clipboard():
    if not _has_consent():
        return jsonify(error="consent_required"), 403
    payload = request.get_json(silent=True) or {}
    # TODO: decrypt, redact, persist
    return jsonify(status="accepted", length=len(payload.get("text", ""))), 202
