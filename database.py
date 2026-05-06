from __future__ import annotations

import hashlib
import sqlite3
from datetime import datetime
from pathlib import Path


DB_PATH = Path("data/einkaufsapp.db")


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS shopping_lists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                list_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                quantity TEXT,
                category TEXT,
                is_done INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                FOREIGN KEY (list_id) REFERENCES shopping_lists(id) ON DELETE CASCADE
            );
            """
        )
        ensure_column(conn, "items", "category", "TEXT")


def ensure_column(conn: sqlite3.Connection, table_name: str, column_name: str, definition: str) -> None:
    columns = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
    if any(column["name"] == column_name for column in columns):
        return

    conn.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {definition}")


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def create_user(username: str, password: str) -> tuple[bool, str]:
    username = username.strip()
    if not username or not password:
        return False, "Benutzername und Passwort duerfen nicht leer sein."

    try:
        with get_connection() as conn:
            conn.execute(
                """
                INSERT INTO users (username, password_hash, created_at)
                VALUES (?, ?, ?)
                """,
                (username, hash_password(password), now_iso()),
            )
        return True, "Registrierung erfolgreich. Du kannst dich jetzt einloggen."
    except sqlite3.IntegrityError:
        return False, "Dieser Benutzername ist bereits vergeben."


def authenticate_user(username: str, password: str) -> sqlite3.Row | None:
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT id, username
            FROM users
            WHERE username = ? AND password_hash = ?
            """,
            (username.strip(), hash_password(password)),
        ).fetchone()


def create_shopping_list(user_id: int, name: str) -> None:
    name = name.strip()
    if not name:
        return

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO shopping_lists (user_id, name, created_at)
            VALUES (?, ?, ?)
            """,
            (user_id, name, now_iso()),
        )


def update_shopping_list(user_id: int, list_id: int, name: str) -> None:
    name = name.strip()
    if not name:
        return

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE shopping_lists
            SET name = ?
            WHERE id = ? AND user_id = ?
            """,
            (name, list_id, user_id),
        )


def delete_shopping_list(user_id: int, list_id: int) -> None:
    with get_connection() as conn:
        conn.execute(
            """
            DELETE FROM shopping_lists
            WHERE id = ? AND user_id = ?
            """,
            (list_id, user_id),
        )


def get_shopping_lists(user_id: int) -> list[sqlite3.Row]:
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT
                shopping_lists.id,
                shopping_lists.name,
                shopping_lists.created_at,
                COUNT(items.id) AS item_count,
                SUM(CASE WHEN items.is_done = 0 THEN 1 ELSE 0 END) AS open_count
            FROM shopping_lists
            LEFT JOIN items ON items.list_id = shopping_lists.id
            WHERE shopping_lists.user_id = ?
            GROUP BY shopping_lists.id
            ORDER BY shopping_lists.created_at DESC
            """,
            (user_id,),
        ).fetchall()


def get_list_for_user(user_id: int, list_id: int) -> sqlite3.Row | None:
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT id, name
            FROM shopping_lists
            WHERE id = ? AND user_id = ?
            """,
            (list_id, user_id),
        ).fetchone()


def add_item(list_id: int, name: str, quantity: str, category: str) -> None:
    name = name.strip()
    if not name:
        return

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO items (list_id, name, quantity, category, is_done, created_at)
            VALUES (?, ?, ?, ?, 0, ?)
            """,
            (list_id, name, quantity.strip(), category.strip(), now_iso()),
        )


def get_items(list_id: int) -> list[sqlite3.Row]:
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT id, name, quantity, category, is_done, created_at
            FROM items
            WHERE list_id = ?
            ORDER BY is_done ASC, category ASC, created_at DESC
            """,
            (list_id,),
        ).fetchall()


def update_item(item_id: int, name: str, quantity: str, category: str) -> None:
    name = name.strip()
    if not name:
        return

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE items
            SET name = ?, quantity = ?, category = ?
            WHERE id = ?
            """,
            (name, quantity.strip(), category.strip(), item_id),
        )


def delete_item(item_id: int) -> None:
    with get_connection() as conn:
        conn.execute(
            """
            DELETE FROM items
            WHERE id = ?
            """,
            (item_id,),
        )


def set_item_done(item_id: int, is_done: bool) -> None:
    with get_connection() as conn:
        conn.execute(
            """
            UPDATE items
            SET is_done = ?
            WHERE id = ?
            """,
            (1 if is_done else 0, item_id),
        )
