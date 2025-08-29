import os
import pytest
from app import create_app


@pytest.fixture()
def app():
    os.environ.setdefault("JWT_SECRET_KEY", "test-secret")
    test_app = create_app()
    test_app.config.update(TESTING=True)
    yield test_app


@pytest.fixture()
def client(app):
    return app.test_client()
