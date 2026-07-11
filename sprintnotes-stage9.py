# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: SprintNotes
def sort_entries(entries, key="date", reverse=False):
    sort_keys = {
        "title": lambda e: e.get("title", "").lower(),
        "date": lambda e: e.get("created_at") or e.get("_date"),
        "priority": lambda e: e.get("priority", 3),
        "updated": lambda e: e.get("last_updated_at") or e.get("_updated"),
    }
    k = sort_keys.get(key, sort_keys["date"])
    return sorted(entries, key=k, reverse=reverse)
