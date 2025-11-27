from flask_login import current_user
from werkzeug.security import generate_password_hash

from src.models import User


def test_user_loader(app, client, db):
    user = User(
        username="loader",
        email="loader@example.com",
        password_hash=generate_password_hash("123")
    )
    db.session.add(user)
    db.session.commit()

    with client:
        client.post("/login", data={
            "username": "loader",
            "password": "123"
        })

        assert current_user.is_authenticated
        assert current_user.username == "loader"
