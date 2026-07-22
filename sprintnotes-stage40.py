# === Stage 40: Add plain text report export ===
# Project: SprintNotes
def export_to_text(sprint):
    """Export a Sprint journal to plain text."""
    out = []
    header = f"Sprint: {sprint.get('name', 'Unnamed')}\nDate: {sprint.get('date', '')}\n"
    out.append(header)

    if sprint.get("backlog"):
        out.append("\n--- Backlog ---")
        for item in sprint["backlog"]:
            status = item.get("status", "pending").upper()
            priority = item.get("priority", 3)
            desc = item.get("description", "")
            line = f"#{item['id']} [{priority}] {desc} [Status: {status}]"
            out.append(line)

    if sprint.get("daily_notes"):
        out.append("\n--- Daily Notes ---")
        for note in sprint["daily_notes"]:
            date = note.get("date", "")
            text = note.get("text", "")
            out.append(f"\n[{date}] {text}")

    if sprint.get("checkpoints"):
        out.append("\n--- Checkpoints ---")
        for cp in sprint["checkpoints"]:
            title = cp.get("title", "")
            result = "✓" if cp.get("passed", True) else "✗"
            out.append(f"[{result}] {title}")

    if sprint.get("delivery_summary"):
        out.append("\n--- Delivery Summary ---")
        summary = sprint["delivery_summary"]
        done = len(summary.get("delivered", []))
        total = len(summary.get("planned", [])) + done
        metric = f"{done}/{total}" if total else "N/A"
        out.append(f"Delivered: {metric}")

    return "\n".join(out)
