import sqlite3
from pathlib import Path
from fastapi import HTTPException
from app.models import TaskCreate, TaskUpdate

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "tasks.db"


def _get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    DATA_DIR.mkdir(exist_ok=True)
    with _get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                title     TEXT    NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)


init_db()


def _row_to_dict(row: sqlite3.Row) -> dict:
    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"]),
    }


def list_tasks() -> list:
    with _get_connection() as conn:
        rows = conn.execute(
            "SELECT id, title, completed FROM tasks ORDER BY id"
        ).fetchall()
    return [_row_to_dict(row) for row in rows]


def create_task(task_create: TaskCreate) -> dict:
    with _get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, ?)",
            (task_create.title, int(task_create.completed)),
        )
        new_id = cursor.lastrowid
    return {
        "id": new_id,
        "title": task_create.title,
        "completed": task_create.completed,
    }


def update_task(task_id: int, task_update: TaskUpdate) -> dict:
    with _get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
            (task_update.title, int(task_update.completed), task_id),
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        row = conn.execute(
            "SELECT id, title, completed FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
    return _row_to_dict(row)


def delete_task(task_id: int) -> None:
    with _get_connection() as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")


def reset_state() -> None:
    with _get_connection() as conn:
        conn.execute("DELETE FROM tasks")
        conn.execute("DELETE FROM sqlite_sequence WHERE name='tasks'")
