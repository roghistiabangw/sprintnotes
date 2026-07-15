# === Stage 18: Add an activity log with timestamps and action names ===
# Project: SprintNotes
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, timestamp=None):
        if timestamp is None:
            import datetime as dt
            timestamp = dt.datetime.now()
        entry = {"timestamp": timestamp, "action": action}
        self.entries.append(entry)
        return entry

    def get_entries(self):
        return list(self.entries)

    def __str__(self):
        lines = ["Activity Log"] + [f"{e['timestamp']} - {e['action']}" for e in self.entries]
        return "\n".join(lines) if lines else "No activities recorded."
