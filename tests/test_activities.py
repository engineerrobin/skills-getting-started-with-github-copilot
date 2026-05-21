from fastapi.testclient import TestClient

from src.app import app


def test_get_activities_returns_data():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
    assert "max_participants" in data["Chess Club"]
