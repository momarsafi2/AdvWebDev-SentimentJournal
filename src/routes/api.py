from collections import Counter

from flask import Blueprint, jsonify
from flask_login import login_required, current_user

from ..models import JournalEntry

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.get("/sentiment-summary")
@login_required
def sentiment_summary():
 
    entries = JournalEntry.query.filter_by(user_id=current_user.id).all()

    labels = [e.sentiment_label for e in entries if e.sentiment_label]
    scores = [e.sentiment_score for e in entries if e.sentiment_score is not None]

    counts = Counter(labels)
    avg = sum(scores) / len(scores) if scores else 0.0

    return jsonify({
        "total": len(entries),
        "by_label": counts,
        "average_score": avg,
    })
