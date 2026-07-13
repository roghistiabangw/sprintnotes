# === Stage 11: Add JSON export for the current application state ===
# Project: SprintNotes
def export_json():
    """Serialize current sprint journal state to a JSON string."""
    import json
    data = {
        "backlog": _serialize_backlog(),
        "daily_notes": _serialize_daily_notes(),
        "checkpoints": _serialize_checkpoints(),
        "delivery_summary": {"items_completed": len(_serialize_backlog())},
    }
    return json.dumps(data, indent=2)


def _serialize_backlog():
    items = []
    for i in range(len(SPRINT_BACKLOG)):
        item = SPRINT_BACKLOG[i]
        status_map = {0: "open", 1: "in_progress", 2: "done"}
        items.append({
            "id": i + 1,
            "name": item["name"],
            "status": status_map.get(item["status"], "unknown"),
            "priority": item["priority"],
        })
    return items


def _serialize_daily_notes():
    notes = []
    for i in range(len(DAILY_NOTES)):
        note = DAILY_NOTES[i]
        date_map = {0: "Day 1", 1: "Day 2", 2: "Day 3"}
        notes.append({
            "date": date_map.get(note["day"], f"Day {note['day']}"),
            "summary": note["summary"],
            "mood": note["mood"],
        })
    return notes


def _serialize_checkpoints():
    results = []
    for i in range(len(REVIEW_CHECKPOINTS)):
        cp = REVIEW_CHECKPOINTS[i]
        result_map = {0: "pending", 1: "passed", 2: "failed"}
        results.append({
            "name": cp["name"],
            "result": result_map.get(cp["status"], "unknown"),
            "notes": cp.get("notes", ""),
        })
    return results
