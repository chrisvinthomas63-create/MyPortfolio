"""
app.py - the Flask backend of the portfolio website.

What this file does:
  1. Creates the Flask application.
  2. Creates the SQLite database + the `messages` table (first run only).
  3. Shows the single-page website  ->  route  "/"
  4. Receives the contact form       ->  route  "/contact"  (validates + saves)
  5. Lets visitors download the CV   ->  route  "/download-resume"

Run it with:   python app.py
"""

import os
import re
import sqlite3
from datetime import datetime

from flask import (
    Flask,
    abort,
    jsonify,
    render_template,
    request,
    send_from_directory,
)

from portfolio_data import ABOUT,CERTIFICATES, EDUCATION, PROFILE, PROJECTS, SKILLS

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024  # reject requests bigger than 64 KB

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------
def get_connection():
    """Open a connection to the SQLite database file."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the messages table if it does not exist yet."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                name       TEXT NOT NULL,
                email      TEXT NOT NULL,
                subject    TEXT NOT NULL,
                message    TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def save_message(name, email, subject, message):
    """Insert one contact message. '?' placeholders keep the query safe."""
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO messages (name, email, subject, message, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (name, email, subject, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
def validate_contact(name, email, subject, message):
    """Return a dictionary of {field: error message}. Empty dict = all good."""
    errors = {}

    if not name:
        errors["name"] = "Please enter your name."
    elif len(name) < 2 or len(name) > 80:
        errors["name"] = "Name must be between 2 and 80 characters."

    if not email:
        errors["email"] = "Please enter your email address."
    elif len(email) > 120 or not EMAIL_PATTERN.match(email):
        errors["email"] = "Please enter a valid email address."

    if not subject:
        errors["subject"] = "Please enter a subject."
    elif len(subject) < 3 or len(subject) > 120:
        errors["subject"] = "Subject must be between 3 and 120 characters."

    if not message:
        errors["message"] = "Please write a message."
    elif len(message) < 10:
        errors["message"] = "Message is too short (at least 10 characters)."
    elif len(message) > 2000:
        errors["message"] = "Message is too long (maximum 2000 characters)."

    return errors


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    """Show the portfolio. All content comes from portfolio_data.py."""
    categories = []
    for project in PROJECTS:
        if project["category"] not in categories:
            categories.append(project["category"])

    return render_template(
        "index.html",
        profile=PROFILE,
        about=ABOUT,
        skills=SKILLS,
        projects=PROJECTS,
        project_categories=categories,
        education=EDUCATION,
        certificates=CERTIFICATES,
        year=datetime.now().year,
    )


@app.route("/contact", methods=["POST"])
def contact():
    """Receive the contact form, validate it, save it, answer with JSON."""
    # Hidden "honeypot" field: real people never fill it, spam bots do.
    if request.form.get("website", "").strip():
        return jsonify(success=True, message="Thank you! Your message has been sent.")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    errors = validate_contact(name, email, subject, message)
    if errors:
        return (
            jsonify(success=False, message="Please fix the highlighted fields.", errors=errors),
            400,
        )

    try:
        save_message(name, email, subject, message)
    except sqlite3.Error:
        return (
            jsonify(success=False, message="Sorry, something went wrong on the server. Please try again."),
            500,
        )

    return jsonify(success=True, message="Thank you! Your message has been sent successfully.")


@app.route("/download-resume")
def download_resume():
    """Send the resume PDF stored in static/resume/ as a download."""
    folder = os.path.join(app.static_folder, "resume")
    filename = PROFILE["resume_file"]
    if not os.path.isfile(os.path.join(folder, filename)):
        abort(404)
    nice_name = PROFILE["name"].replace(" ", "_") + "_Resume.pdf"
    return send_from_directory(folder, filename, as_attachment=True, download_name=nice_name)


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html", profile=PROFILE), 404


@app.errorhandler(413)
def too_large(_error):
    return jsonify(success=False, message="Your message is too large."), 413


# ---------------------------------------------------------------------------
# Start the app
# ---------------------------------------------------------------------------
init_db()  # make sure the database and table exist

if __name__ == "__main__":
    # debug=True reloads the server automatically when you save a file.
    # Turn it off (debug=False) if you ever put the site on the internet.
    app.run(debug=True)
