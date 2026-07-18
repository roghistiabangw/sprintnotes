# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: SprintNotes
def upcoming_items(items, days=7):
    """Return items whose due date falls within the next `days` calendar days."""
    today = datetime.date.today()
    return [i for i in items if (today + timedelta(days=i.get("day", 0))) <= today + timedelta(days=days)]

def remind_on_due(items, deadline=None):
    """Return items due on or before `deadline`; defaults to the next 24h."""
    if deadline is None:
        return [i for i in items if datetime.date.today() - timedelta(hours=i.get("day", 0)) <= datetime.date.today()]
    return [i for i in items if datetime.date.fromisoformat(i["due"]) <= datetime.date.fromisoformat(deadline)]

def next_review(items, days=14):
    """Return the closest review checkpoint within `days`."""
    today = datetime.date.today()
    candidates = [(datetime.date.fromisoformat(i["review_date"]) - today).total_seconds() for i in items if i.get("review")]
    if not candidates: return []
    return [i for i, s in zip(items, sorted(candidates)) if abs(s) <= days * 86400]
