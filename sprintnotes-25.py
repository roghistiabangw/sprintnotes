# === Stage 25: Add daily summary calculations ===
# Project: SprintNotes
def daily_summary(daily_notes, backlog_items):
    """Generate a compact daily summary from notes and backlog items."""
    total_backlog = len(backlog_items)
    completed = sum(1 for item in backlog_items if item.get('status') == 'completed')
    
    active = total_backlog - completed
    note_count = len(daily_notes)
    
    priority_tasks = [item for item in backlog_items if item.get('priority', 'low') != 'low']
    high_priority_active = sum(1 for task in priority_tasks if task['status'] != 'completed')
    
    return {
        'total_backlog': total_backlog,
        'completed': completed,
        'active': active,
        'note_count': note_count,
        'high_priority_active': high_priority_active,
        'completion_rate': round((completed / total_backlog) * 100, 2) if total_backlog > 0 else 0
    }
