import os
import pytest
from app import create_app


@pytest.fixture()
def app(tmp_path):
    os.environ.setdefault("JWT_SECRET_KEY", "test-secret")
    test_app = create_app()
    test_app.config.update(TESTING=True)
    # Force instance path to temporary directory for persistence tests
    test_app.config["INSTANCE_PATH"] = str(tmp_path)
    yield test_app


@pytest.fixture()
def client(app):
    return app.test_client()
