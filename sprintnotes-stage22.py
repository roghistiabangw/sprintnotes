# === Stage 22: Add favorite records and quick favorite listing ===
# Project: SprintNotes
import json, os

class SprintNotes:
    def __init__(self):
        self.data = {"backlog": [], "daily_notes": {}, "review_checkpoints": [], "delivery_summaries": []}
        self.file_path = "sprint_notes.json"
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump(self.data, f)

    def add_backlog_item(self, description, priority="medium"):
        item = {"description": description, "priority": priority}
        self.data["backlog"].append(item)
        self.save()

    def add_daily_note(self, date, note):
        self.data["daily_notes"][date] = note
        self.save()

    def add_review_checkpoint(self, topic, status, notes=""):
        checkpoint = {"topic": topic, "status": status, "notes": notes}
        self.data["review_checkpoints"].append(checkpoint)
        self.save()

    def add_delivery_summary(self, sprint_name, items_completed=0):
        summary = {"sprint_name": sprint_name, "items_completed": items_completed}
        self.data["delivery_summaries"].append(summary)
        self.save()

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def get_backlog(self):
        return self.data["backlog"]

    def get_daily_notes(self):
        return self.data["daily_notes"]

    def get_review_checkpoints(self):
        return self.data["review_checkpoints"]

    def get_delivery_summaries(self):
        return self.data["delivery_summaries"]

    def add_favorite_record(self, record_id, description, category, notes=""):
        favorite = {"record_id": record_id, "description": description, "category": category, "notes": notes}
        if "favorites" not in self.data:
            self.data["favorites"] = []
        self.data["favorites"].append(favorite)
        self.save()

    def get_favorites(self):
        return self.data.get("favorites", [])

    def remove_favorite(self, record_id):
        if "favorites" in self.data:
            self.data["favorites"] = [f for f in self.data["favorites"] if f["record_id"] != record_id]
            self.save()

    def search_favorites(self, keyword):
        results = []
        for fav in self.get_favorites():
            if keyword.lower() in fav["description"].lower() or keyword.lower() in fav["category"].lower():
                results.append(fav)
        return results
