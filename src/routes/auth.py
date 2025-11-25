from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from ..models import User
from ..app import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.get("/register")
def register_get():
    return render_template("register.html")

@auth_bp.post("/register")
def register_post():
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    if not username or not email or not password:
        flash("All fields are required.", "error")
        return redirect(url_for("auth.register_get"))

    existing = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()
    if existing:
        flash("Username or email already in use.", "error")
        return redirect(url_for("auth.register_get"))

    user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password),
    )
    db.session.add(user)
    db.session.commit()

    flash("Account created. Please log in.", "success")
    return redirect(url_for("auth.login_get"))

@auth_bp.get("/login")
def login_get():
    return render_template("login.html")

@auth_bp.post("/login")
def login_post():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        flash("Invalid username or password.", "error")
        return redirect(url_for("auth.login_get"))

    login_user(user)
    return redirect(url_for("main.index"))

@auth_bp.post("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
