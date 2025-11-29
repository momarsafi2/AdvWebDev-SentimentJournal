from collections import Counter

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user

from ..extensions import db
from ..models import JournalEntry
from ..external_api import fetch_random_quote
from ..sentiment import analyze_sentiment

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.get("/entries")
@login_required
def api_get_entries():
    """Return all journal entries for the current user as JSON."""
    entries = (
        JournalEntry.query
        .filter_by(user_id=current_user.id)
        .order_by(JournalEntry.created_at.desc())
        .all()
    )

    data = [
        {
            "id": e.id,
            "text": e.text,
            "sentiment_score": e.sentiment_score,
            "sentiment_label": e.sentiment_label,
            "created_at": e.created_at.isoformat() if e.created_at else None,
        }
        for e in entries
    ]
    return jsonify(data), 200

@api_bp.post("/entries")
@login_required
def api_create_entry():
    """Create a new journal entry via JSON payload."""
    payload = request.get_json() or {}
    text = (payload.get("text") or "").strip()

    if not text:
        return jsonify({"error": "Field 'text' is required."}), 400

    score, label = analyze_sentiment(text)

    entry = JournalEntry(
        user_id=current_user.id,
        text=text,
        sentiment_score=score,
        sentiment_label=label,
    )
    db.session.add(entry)
    db.session.commit()

    return (
        jsonify(
            {
                "id": entry.id,
                "text": entry.text,
                "sentiment_score": entry.sentiment_score,
                "sentiment_label": entry.sentiment_label,
                "created_at": entry.created_at.isoformat()
                if entry.created_at
                else None,
            }
        ),
        201,
    )

@api_bp.get("/sentiment-summary")
@login_required
def sentiment_summary():
    entries = JournalEntry.query.filter_by(user_id=current_user.id).all()

    labels = [e.sentiment_label for e in entries if e.sentiment_label]
    scores = [e.sentiment_score for e in entries if e.sentiment_score is not None]

    counts = Counter(labels)
    avg = sum(scores) / len(scores) if scores else 0.0

    return jsonify(
        {
            "total": len(entries),
            "by_label": counts,
            "average_score": avg,
        }
    )

@api_bp.get("/quote")
def quote():
    quote_data = fetch_random_quote()
    return jsonify(quote_data), 200
