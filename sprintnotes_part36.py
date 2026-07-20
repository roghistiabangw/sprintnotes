# === Stage 36: Add templates for quickly creating common records ===
# Project: SprintNotes
TEMPLATES = {
    "backlog_item": f"""item_name: """,
    "daily_note": f"""date: YYYY-MM-DD
note: """,
    "review_checkpoint": f"""checkpoint_type: review
status: planned | completed | blocked
notes: """,
    "delivery_summary": f"""sprint_end: YYYY-MM-DD
items_delivered: []
lessons_learned: """,
}
