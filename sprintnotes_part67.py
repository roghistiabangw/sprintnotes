# === Stage 67: Add a function that returns key project metrics ===
# Project: SprintNotes
def project_metrics(backlog, daily_notes, checkpoints):
    """Return key sprint metrics as a dict."""
    total_items = len(backlog)
    completed = sum(1 for item in backlog if item.get("status") == "done")
    pending = total_items - completed
    completion_rate = (completed / total_items * 100) if total_items else 0.0

    active_days = len(daily_notes)
    check_passed = sum(1 for cp in checkpoints if cp.get("passed"))
    checkpoint_pass_rate = (check_passed / len(checkpoints) * 100) if checkpoints else 0.0

    daily_avg = active_days > 0 and active_days / max(len(daily_notes), 1) or 0.0

    metrics = {
        "total_backlog_items": total_items,
        "completed_items": completed,
        "pending_items": pending,
        "completion_rate_pct": round(completion_rate, 2),
        "active_days": active_days,
        "checkpoints_passed": check_passed,
        "checkpoint_pass_rate_pct": round(checkpoint_pass_rate, 2),
    }
    return metrics
