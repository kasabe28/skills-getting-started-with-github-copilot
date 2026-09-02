from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "michael@mergington.edu"

    response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": email},
    )

    assert response.status_code == 200
    assert email not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_participant_raises_404_when_email_not_found():
    response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": "not-found@mergington.edu"},
    )

    assert response.status_code == 404
