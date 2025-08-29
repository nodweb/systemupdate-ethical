from flask import Flask, jsonify
from .extensions import jwt
from .routes.data import data_bp
import os


def create_app() -> Flask:
    app = Flask(__name__)

    # Very simple JWT config for skeleton; replace with secure secret management
    app.config.setdefault("JWT_SECRET_KEY", "change-me-dev-only")

    jwt.init_app(app)

    # Blueprints
    app.register_blueprint(data_bp, url_prefix="/api")

    # Dev-only helpers (guarded by env flags)
    if os.getenv("DEV_JWT_ENABLED", "false").lower() in ("1", "true", "yes"):
        from .routes.dev import dev_bp
        app.register_blueprint(dev_bp, url_prefix="/dev")

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    return app
