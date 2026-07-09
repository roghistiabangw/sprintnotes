# === Stage 4: Implement create operations for the primary records ===
# Project: SprintNotes
class SprintNote:
    def __init__(self, title):
        self.title = title

    def create_backlog_item(self, description, priority="medium"):
        item = BacklogItem(description=description, priority=priority)
        self.backlog.append(item)
        return item

    def create_daily_note(self, date_str, content):
        note = DailyNote(date=date_str, content=content)
        self.daily_notes.append(note)
        return note

    def create_review_checkpoint(self, name, status="open"):
        checkpoint = ReviewCheckpoint(name=name, status=status)
        self.checkpoints.append(checkpoint)
        return checkpoint

    def create_delivery_summary(self):
        summary = DeliverySummary()
        self.summaries.append(summary)
        return summary
