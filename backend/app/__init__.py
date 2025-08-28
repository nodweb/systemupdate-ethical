from flask import Flask, jsonify
from .extensions import jwt
from .routes.data import data_bp


def create_app() -> Flask:
    app = Flask(__name__)

    # Very simple JWT config for skeleton; replace with secure secret management
    app.config.setdefault("JWT_SECRET_KEY", "change-me-dev-only")

    jwt.init_app(app)

    # Blueprints
    app.register_blueprint(data_bp, url_prefix="/api")

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    return app
