# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: SprintNotes
import json, random, datetime

class SprintNotes:
    def __init__(self):
        self.backlog = []
        self.notes = {}  # date -> note text
        self.checkpoints = []  # list of review results
        self.delivery = {"items": [], "summary": ""}

    def add_backlog_item(self, title, priority="medium"):
        item = {"id": len(self.backlog)+1, "title": title, "priority": priority, "status": "open"}
        self.backlog.append(item)
        return item

    def daily_note(self, date_str, text):
        self.notes[date_str] = text

    def checkpoint_review(self, items, passed=True, feedback=""):
        self.checkpoints.append({"items": [i["id"] for i in items], "passed": passed, "feedback": feedback})

    def mark_delivered(self, item_id, date=None):
        if not isinstance(item_id, int) or item_id < 1: return None
        idx = next((i for i, x in enumerate(self.backlog) if x["id"] == item_id), None)
        if idx is None: return None
        self.backlog[idx]["status"] = "done"
        date = date or datetime.date.today().isoformat()
        entry = {"item": item_id, "date": date, "note": f"Delivered {self.backlog[idx]['title']}"}
        if len(self.delivery["items"]) < 20:
            self.delivery["items"].append(entry)
        return entry

demo = SprintNotes()
demo.add_backlog_item("Design sprint board", priority="high")
demo.add_backlog_item("Setup CI pipeline")
demo.daily_note("2024-01-07", "Sprint planning: 3 items for the next 2 weeks.")
demo.checkpoint_review([demo.backlog[0]], passed=True, feedback="Board ready, team aligned.")
done = demo.mark_delivered(1)
