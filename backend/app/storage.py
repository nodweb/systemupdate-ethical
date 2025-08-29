import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict
from flask import current_app


def _instance_root() -> Path:
    # Allow tests to override via config; otherwise use app.instance_path
    cfg_path = current_app.config.get("INSTANCE_PATH")
    if cfg_path:
        return Path(cfg_path)
    return Path(current_app.instance_path)


def save_payload(kind: str, device_id: str, payload: Dict[str, Any], envelope: bool = False) -> Path:
    """
    Persist payload JSON under instance/uploads/<kind>/<YYYY-MM-DD>/
    Filename: <ts>_<device>_<env|plain>.json
    Returns the full file Path.
    """
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    date_dir = datetime.utcnow().strftime("%Y-%m-%d")
    safe_device = "".join(c for c in device_id if c.isalnum() or c in ("-", "_"))[:64] or "unknown"
    suffix = "env" if envelope else "plain"
    root = _instance_root() / "uploads" / kind / date_dir
    os.makedirs(root, exist_ok=True)
    file_path = root / f"{ts}_{safe_device}_{suffix}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    return file_path
