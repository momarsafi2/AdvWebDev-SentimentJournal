from werkzeug.security import generate_password_hash

from src.models import JournalEntry, User


def test_create_user(db):
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash=generate_password_hash("password123")
    )
    db.session.add(user)
    db.session.commit()

    assert User.query.count() == 1
    assert user.id is not None

def test_create_journal_entry(db):
    user = User(
        username="writer",
        email="writer@example.com",
        password_hash=generate_password_hash("pass123")
    )
    db.session.add(user)
    db.session.commit()

    entry = JournalEntry(
        user_id=user.id,
        text="Feeling good.",
        sentiment_score=0.8,
        sentiment_label="POSITIVE"
    )
    db.session.add(entry)
    db.session.commit()

    assert JournalEntry.query.count() == 1
    assert entry.user.username == "writer"
