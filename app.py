import sqlite3
from datetime import datetime
from random import randint
from flask import Flask, redirect, render_template, request, session

from flask_session import Session

app = Flask(__name__)

conn = sqlite3.connect("session.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Button (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    button INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)""")

cur.execute("""
CREATE TABLE IF NOT EXISTS PageView (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    page TEXT,
    time_spent REAL,
    start_time DATETIME
)""")
conn.commit()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route("/contact_button")
def button_tracking():
    if "id" not in session:
        return

    session_id = session.get("id")
    cur.execute(
        "INSERT INTO Button (session_id, button) VALUES (?, ?)", (session_id, 1)
    )
    conn.commit()

    return redirect("/contact")

@app.before_request
def assign_id():
    if "id" not in session:
        session["id"] = randint(1_000_000, 9_999_999)
        return

def log_data():
    if not all([key in session for key in ("id", "start_time", "previous_path")]):
        return
    
    session_id = session.get("id")
    start_time = session.get("start_time")
    previous_path = session.get("previous_path")

    time_spent = (datetime.now() - start_time).total_seconds()

    cur.execute(
        "INSERT INTO PageView (session_id, page, time_spent, start_time) VALUES (?, ?, ?, ?)",
        (session_id, previous_path, time_spent, start_time),
    )
    conn.commit()
    return


@app.after_request
def track_time(response):
    if request.path == "/":
        log_data()
        # Update start_time and previous_path
        session["start_time"] = datetime.now()
        session["previous_path"] = "HomePage"

    if request.path == "/about":
        log_data()
        # Update start_time and previous_path
        session["start_time"] = datetime.now()
        session["previous_path"] = "About"

    if request.path == "/contact":
        log_data()
        session["start_time"] = datetime.now()
        session["previous_path"] = "Contact"

    return response

if __name__ == "__main__":
    app.run(debug=True) # Adding debug=True applies your changes in real time.
