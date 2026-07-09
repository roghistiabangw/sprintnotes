# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: SprintNotes
import json, os

def update_sprint_note(repo_path: str, note_id: int, fields: dict) -> dict:
    """Update an existing sprint note by partial fields; returns the merged record."""
    file = repo_path / "sprint_notes.json"
    if not file.exists():
        return {"error": f"No notes file at {file}", "status": 404}

    with open(file, "r") as f:
        records = json.load(f)

    try:
        record = next((n for n in records if n["id"] == note_id), None)
    except StopIteration:
        return {"error": f"Note {note_id} not found", "status": 404}

    if not fields:
        return record

    update_fields = {}
    for key, value in fields.items():
        if key == "id":
            continue
        if value is None or value == "":
            continue
        update_fields[key] = value

    if not update_fields:
        return {"error": "No valid fields to update", "status": 400}

    record.update(update_fields)
    with open(file, "w") as f:
        json.dump(records, f, indent=2)

    return {**record, "_updated": True}
