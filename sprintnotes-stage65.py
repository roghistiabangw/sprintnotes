# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: SprintNotes
import os, sys, datetime

class SprintJournal:
    def __init__(self):
        self.backlog = []
        self.daily_notes = {}
        self.checkpoints = []
        self.delivery_summary = None
        self.project_dir = "sprint_journal"

    def add_backlog_item(self, title, priority="medium"):
        item = {"title": title, "priority": priority, "status": "open", "date": datetime.date.today().isoformat()}
        self.backlog.append(item)
        return item

    def add_daily_note(self, date_str, note):
        if date_str not in self.daily_notes:
            self.daily_notes[date_str] = []
        self.daily_notes[date_str].append(note)

    def set_checkpoint(self, sprint_num, review_type="retro", notes=""):
        self.checkpoints.append({"sprint": sprint_num, "type": review_type, "notes": notes})

    def finalize_sprint(self):
        if not self.checkpoints:
            raise ValueError("No checkpoints defined.")
        done = [i for i in self.backlog if i["status"] == "done"]
        open_items = [i for i in self.backlog if i["status"] != "done"]
        today = datetime.date.today().isoformat()
        summary = {
            "sprint_id": len(self.checkpoints),
            "date": today,
            "items_done": done,
            "items_remaining": open_items,
            "review_notes": self.checkpoints[-1]["notes"]
        }
        self.delivery_summary = summary

    def export_to_json(self):
        import json
        return json.dumps({
            "backlog": self.backlog,
            "daily_notes": self.daily_notes,
            "checkpoints": self.checkpoints,
            "delivery_summary": self.delivery_summary
        }, indent=2)
