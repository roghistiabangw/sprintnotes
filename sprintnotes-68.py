# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: SprintNotes
def generate_changelog(activity_log):
    """Generate a compact changelog from an activity log."""
    entries = []
    for item in activity_log:
        entry = f"- {item['date']} — {item.get('summary', 'No summary')}"
        if item.get('type'):
            tag = f" [{item['type']}]".capitalize()
            entry += tag
        entries.append(entry)
    return "\n".join(entries)
