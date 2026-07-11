# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: SprintNotes
def format_backlog_item(item):
    return f"[{item['priority']}] {item['title']} — {item.get('status', 'pending')}"

def format_daily_note(date, entries):
    lines = [f"📝 {date}"]
    for entry in entries:
        tag = entry.get("tag", "general")
        text = entry["text"].replace("\n", "\n  ")
        if tag == "decision":
            lines.append(f"  ⚡ Decision: {text}")
        elif tag == "issue":
            lines.append(f"  🐛 Issue: {text}")
        else:
            lines.append(f"  • {text}")
    return "\n".join(lines)

def format_review_checkpoint(checkpoint):
    parts = [f"🔍 Checkpoint: {checkpoint['date']}"]
    for k, v in checkpoint.items():
        if k not in ("title", "date"):
            parts.append(f"  {k}: {v}")
    return "\n".join(parts)

def format_delivery_summary(summary):
    lines = [f"📦 Delivery: {summary['sprint']}"]
    for key, val in summary.items():
        if key not in ("title", "sprint"):
            lines.append(f"  {key}: {val}")
    return "\n".join(lines)
