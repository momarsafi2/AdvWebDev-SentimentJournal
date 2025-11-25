from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

from ..models import JournalEntry
from ..extensions import db
from ..sentiment import analyze_sentiment

entries_bp = Blueprint("entries", __name__, url_prefix="/entries")

@entries_bp.get("/")
@login_required
def list_entries():
    entries = (
        JournalEntry.query
        .filter_by(user_id=current_user.id)
        .order_by(JournalEntry.created_at.desc())
        .all()
    )
    return render_template("entries.html", entries=entries)

@entries_bp.get("/new")
@login_required
def new_entry_get():
    return render_template("new_entry.html")

@entries_bp.post("/new")
@login_required
def new_entry_post():
    text = request.form.get("text", "").strip()

    if not text:
        return redirect(url_for("entries.new_entry_get"))

    score, label = analyze_sentiment(text)

    entry = JournalEntry(
        user_id=current_user.id,
        text=text,
        sentiment_score=score,
        sentiment_label=label,
    )
    db.session.add(entry)
    db.session.commit()

    return redirect(url_for("entries.list_entries"))

# Edit
@entries_bp.get("/<int:entry_id>/edit")
@login_required
def edit_entry_get(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        abort(404) 
    return render_template("edit_entry.html", entry=entry)

@entries_bp.post("/<int:entry_id>/edit")
@login_required
def edit_entry_post(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        abort(404)

    text = request.form.get("text", "").strip()
    if not text:
        return redirect(url_for("entries.edit_entry_get", entry_id=entry.id))

    entry.text = text

    score, label = analyze_sentiment(text)
    entry.sentiment_score = score
    entry.sentiment_label = label

    db.session.commit()

    return redirect(url_for("entries.list_entries"))

# Delete
@entries_bp.post("/<int:entry_id>/delete")
@login_required
def delete_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        abort(404)

    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for("entries.list_entries"))
