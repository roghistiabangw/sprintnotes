# === Stage 46: Add a schema version field and migration helper ===
# Project: SprintNotes
def migrate_notes_db(db_path):
    """Migrate SprintNotes DB to schema version 3 by adding a 'schema_version' column."""
    import sqlite3, os
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='notes_db'")
        if not cur.fetchone():
            raise ValueError("notes_db table missing")
        cur.execute("PRAGMA table_info(notes_db)")
        cols = {row[1] for row in cur.fetchall()}
        if "schema_version" not in cols:
            cur.execute("ALTER TABLE notes_db ADD COLUMN schema_version INTEGER DEFAULT 3")
            conn.commit()
    finally:
        conn.close()
