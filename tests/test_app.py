from __future__ import annotations

from reaction_game.app import app


def test_healthcheck():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_score_endpoint():
    client = app.test_client()
    response = client.post("/api/score", json={"score": 12})
    data = response.get_json()

    assert response.status_code == 200
    assert data["score"] == 12
    assert data["performance"] == "average"
