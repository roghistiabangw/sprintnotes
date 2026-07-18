# === Stage 27: Add monthly summary calculations ===
# Project: SprintNotes
def monthly_summary(daily_notes, backlog_items):
    """Compute a compact monthly summary from daily notes and backlog items."""
    month = datetime.now().month
    total_days_worked = sum(1 for note in daily_notes if note.get("date")[:7] == f"{datetime.now().year}-{month:02d}")
    completed_items = [item for item in backlog_items if item["status"] == "done" and item["assigned_month"] == month]
    review_count = sum(1 for note in daily_notes if note.get("type") == "review")
    return {
        "month": f"{datetime.now().year}-{month:02d}",
        "days_worked": total_days_worked,
        "completed_items": len(completed_items),
        "total_backlog": len(backlog_items),
        "reviews_held": review_count
    }
