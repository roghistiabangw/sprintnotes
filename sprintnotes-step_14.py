# === Stage 14: Add file load support with fallback demo data ===
# Project: SprintNotes
def load_file(path: str = "sprint_notes.json") -> dict:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "backlog": [],
            "daily_notes": {},
            "reviews": [],
            "summaries": []
        }
