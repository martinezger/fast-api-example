from fastapi.testclient import TestClient
from setups.app import app
from pytest import fixture


@fixture
def app_client(request):
    request.cls.client = TestClient(app)
    yield
