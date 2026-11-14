"""
view_messages.py - prints every message saved by the contact form.

Run it with:   python view_messages.py
"""

import os
import sqlite3

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")

if not os.path.exists(DATABASE):
    print("No database yet. Start the website once with:  python app.py")
    raise SystemExit

connection = sqlite3.connect(DATABASE)
rows = connection.execute(
    "SELECT id, name, email, subject, message, created_at FROM messages ORDER BY id DESC"
).fetchall()
connection.close()

if not rows:
    print("No messages yet.")
else:
    print(str(len(rows)) + " message(s)\n" + "=" * 60)
    for msg_id, name, email, subject, message, created_at in rows:
        print(f"#{msg_id}  {created_at}")
        print(f"From   : {name} <{email}>")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        print("-" * 60)