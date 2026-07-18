# === Stage 28: Add overdue item detection based on due dates ===
# Project: SprintNotes
def detect_overdue_items(items: list[dict]) -> tuple[list[str], list[dict]]:
    overdue = []
    today = datetime.now().date()
    for item in items:
        due_date = item.get("due_date")
        if isinstance(due_date, str):
            try:
                due_date = datetime.strptime(due_date[:10], "%Y-%m-%d").date()
            except ValueError:
                continue
        elif not isinstance(due_date, date):
            continue
        status = (item.get("status") or "").lower()
        if due_date < today and status != "done":
            overdue.append(item["title"])
