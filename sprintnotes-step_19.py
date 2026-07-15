# === Stage 19: Add undo support for the last simple mutation ===
# Project: SprintNotes
def undo_last_mutation():
    """Undo the last simple mutation by rolling back the most recent change."""
    if not _mutation_history:
        return
    previous_state = _mutation_history.pop()
    current_state = {
        'backlog': _backlog,
        'daily_notes': _daily_notes,
        'review_checkpoints': _review_checkpoints,
        'delivery_summaries': _delivery_summaries,
    }
    if current_state == previous_state:
        return
    _mutation_history.append(current_state)
    for key in ['backlog', 'daily_notes', 'review_checkpoints', 'delivery_summaries']:
        setattr(_sprint_journal, key, getattr(previous_state, key))
