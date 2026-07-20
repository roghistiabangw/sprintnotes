# === Stage 37: Add recommendations for the next useful action ===
# Project: SprintNotes
def suggest_next_action(current_phase, backlog_items, daily_notes):
    """Recommend a useful next step based on sprint phase and recent activity."""
    if current_phase == "planning":
        return "Begin drafting user stories from the top-priority backlog items."
    elif current_phase in ["execution", "daily_work"]:
        note_count = len(daily_notes)
        if note_count < 3:
            return "Write a daily note to track progress and blockers."
        pending = [i for i in backlog_items if not i.get("done")]
        if pending:
            return f"Pick the next unfinished item from the backlog ({pending[0]['title']})."
        else:
            return "Schedule a review checkpoint to assess completed work."
    elif current_phase == "review":
        done_count = sum(1 for i in backlog_items if i.get("done"))
        total = len(backlog_items)
        if done_count < total * 0.8:
            return "Continue working on remaining backlog items before finalizing the sprint."
        else:
            return f"Compile delivery summary — {done_count}/{total} items delivered. Sprint review complete."
    elif current_phase == "planning_next":
        backlog_items = [i for i in backlog_items if not i.get("done")]
        if backlog_items:
            return "Move unfinished items to the next sprint's backlog or escalate as blockers."
        else:
            return "Start planning the next sprint by gathering new requirements and estimating effort."
    else:
        return "Update sprint phase status and re-evaluate priorities."
