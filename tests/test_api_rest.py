import json

from werkzeug.security import generate_password_hash

from src.models import User


def register_and_login(client, db):
    user = User(
        username="apiuser",
        email="api@example.com",
        password_hash=generate_password_hash("password123")
    )
    db.session.add(user)
    db.session.commit()

    client.post("/login", data={
        "username": "apiuser",
        "password": "password123"
    })

    return user

def test_api_get_entries(client, db):
    user = register_and_login(client, db)

    res = client.get("/api/entries")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert isinstance(data, list)

def test_api_create_entry(client, db):
    user = register_and_login(client, db)

    res = client.post("/api/entries", json={
        "text": "Testing API creation"
    })
    assert res.status_code == 201

    data = json.loads(res.data)
    assert "id" in data
    assert data["sentiment_label"] in ["POSITIVE", "NEGATIVE", "NEUTRAL"]
