# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: SprintNotes
def clear_state(confirmation_flag: bool) -> None:
    if confirmation_flag:
        _backlog_items.clear()
        _daily_notes.clear()
        _review_checkpoints.clear()
        _delivery_summaries.clear()
        _current_sprint = Sprint("next")
        print("SprintNotes state cleared.")
