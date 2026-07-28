# === Stage 63: Add relationships between records where useful ===
# Project: SprintNotes
class SprintRecord:
    def __init__(self, record_type, title, description="", date=None):
        self.record_type = record_type  # backlog_item / daily_note / review_checkpoint / delivery_summary
        self.title = title
        self.description = description
        self.date = date or datetime.now().date()

class SprintJournal:
    def __init__(self):
        self.backlog_items = []
        self.daily_notes = []
        self.review_checkpoints = []
        self.delivery_summaries = []
    
    def add_backlog_item(self, title, description="", date=None):
        item = SprintRecord("backlog_item", title, description, date)
        self.backlog_items.append(item)
        return item
    
    def add_daily_note(self, title, description="", date=None):
        note = SprintRecord("daily_note", title, description, date)
        self.daily_notes.append(note)
        return note
    
    def add_review_checkpoint(self, title, description="", date=None):
        checkpoint = SprintRecord("review_checkpoint", title, description, date)
        self.review_checkpoints.append(checkpoint)
        return checkpoint
    
    def add_delivery_summary(self, title, description="", date=None):
        summary = SprintRecord("delivery_summary", title, description, date)
        self.delivery_summaries.append(summary)
        return summary
    
    def get_all_records_by_date_range(self, start_date, end_date):
        all_records = (self.backlog_items + self.daily_notes + 
                       self.review_checkpoints + self.delivery_summaries)
        filtered = [r for r in all_records if start_date <= r.date <= end_date]
        return filtered
    
    def get_backlog_status(self):
        open_count = sum(1 for item in self.backlog_items if "Done" not in item.description and "Closed" not in item.description)
        closed_count = len(self.backlog_items) - open_count
        return {"open": open_count, "closed": closed_count}
    
    def generate_sprint_summary(self):
        total_records = len(self.backlog_items) + len(self.daily_notes) + \
                         len(self.review_checkpoints) + len(self.delivery_summaries)
        backlog_status = self.get_backlog_status()
        return {
            "total_records": total_records,
            "backlog_open": backlog_status["open"],
            "backlog_closed": backlog_status["closed"]
        }
