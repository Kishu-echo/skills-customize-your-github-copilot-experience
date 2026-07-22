import sqlite3
from flask import Flask, g, redirect, render_template_string, request, url_for

app = Flask(__name__)
DATABASE = "database.db"

PAGE_TEMPLATE = """
<!doctype html>
<title>Notes App</title>
<h1>Notes</h1>
<form method="post" action="/{{ url_for('add_note') }}">
  <label for="note">Note:</label>
  <input type="text" name="note" id="note" required>
  <button type="submit">Add Note</button>
</form>
{% if message %}
  <p>{{ message }}</p>
{% endif %}
<ul>
  {% for note in notes %}
    <li>{{ note[1] }}</li>
  {% endfor %}
</ul>
"""


def get_db():
    db = getattr(g, "db", None)
    if db is None:
        db = g.db = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext

def close_db(error=None):
    db = getattr(g, "db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute(
        "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT NOT NULL)"
    )
    db.commit()


@app.route("/", methods=["GET"])
def index():
    init_db()
    db = get_db()
    notes = db.execute("SELECT id, text FROM notes").fetchall()
    return render_template_string(PAGE_TEMPLATE, notes=notes, message="")


@app.route("/add", methods=["POST"])
def add_note():
    note_text = request.form["note"]
    db = get_db()
    db.execute("INSERT INTO notes (text) VALUES (?)", (note_text,))
    db.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
