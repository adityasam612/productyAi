

import sqlite3
from datetime import datetime

DB_PATH = "data/tasks.db"

# ── Create the database & table ─────────────────────────
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT NOT NULL,
            priority  TEXT DEFAULT 'medium',
            due_date  TEXT,
            done      INTEGER DEFAULT 0,
            created   TEXT
        )
    """)
    conn.commit()
    conn.close()



# CREATE — add a new task
def add_task(title, priority="medium", due_date=None):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO tasks (title, priority, due_date, created) VALUES (?,?,?,?)",
        (title, priority, due_date, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

# READ — get all pending or completed tasks
def get_tasks(done=0):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT * FROM tasks WHERE done=? ORDER BY priority",
        (done,)
    ).fetchall()
    conn.close()
    return rows

# UPDATE — mark a task as done
def complete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

# DELETE — remove a task permanently
def delete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()