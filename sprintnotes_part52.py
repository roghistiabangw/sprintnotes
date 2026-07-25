# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: SprintNotes
def get_backlog_item_count(backlog: list[dict]) -> int:
    """Return the number of pending backlog items."""
    return sum(1 for item in backlog if item.get("status") == "pending")


def mark_review_passed(checkpoints: list[dict], review_date: str) -> None:
    """Mark all checkpoints as passed and record the review date."""
    for cp in checkpoints:
        cp["reviewed"] = True
        cp["reviewed_at"] = review_date


def generate_delivery_summary(
    backlog: list[dict], daily_notes: list[dict]
) -> str:
    """Build a compact delivery summary from backlog and daily notes."""
    done = sum(1 for item in backlog if item.get("status") == "done")
    total = len(backlog)
    lines = [f"Delivery Summary — {total} items tracked", f"Completed: {done}/{total}", "---"]
    for note in daily_notes:
        date = note.get("date", "?")
        title = note.get("title", "")
        if title:
            lines.append(f"[{date}] {title}")
    return "\n".join(lines)


def format_sprint_entry(
    sprint_id: str, backlog: list[dict], notes: list[dict]
) -> dict:
    """Return a formatted sprint entry containing summary and details."""
    summary = generate_delivery_summary(backlog, notes)
    return {
        "sprint": sprint_id,
        "summary": summary,
        "backlog_count": len(backlog),
        "notes_count": len(notes),
    }
