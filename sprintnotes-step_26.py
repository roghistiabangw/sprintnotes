# === Stage 26: Add weekly summary calculations ===
# Project: SprintNotes
class WeeklySummary:
    def __init__(self, week_start, completed_items, hours_logged):
        self.week_start = week_start
        self.completed_items = completed_items
        self.hours_logged = hours_logged

    @staticmethod
    def calculate(weeks):
        if not weeks:
            return WeeklySummary(None, [], 0)
        total_hours = sum(w.hours_logged for w in weeks)
        all_completed = [item for w in weeks for item in w.completed_items]
        earliest_start = min(w.week_start for w in weeks)
        latest_end = max(w.week_start + timedelta(days=7) for w in weeks)
        return WeeklySummary(earliest_start, all_completed, total_hours)

    def summary_string(self):
        days_active = (self.week_start + timedelta(days=7)) - self.week_start if self.week_start else 0
        if not self.week_start:
            return "No weekly data available."
        completion_rate = len(self.completed_items) / max(days_active, 1) * 100
        avg_hours = self.hours_logged / max(len(weeks), 1) if self.hours_logged else 0
        return f"Weekly Summary: {self.week_start} - Completed: {len(self.completed_items)} items ({completion_rate:.1f}% rate), Hours logged: {self.hours_logged}, Avg hours per day: {avg_hours:.2f}"
