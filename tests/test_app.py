from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_welcome_root():
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    """Test the health endpoint returns ok status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
