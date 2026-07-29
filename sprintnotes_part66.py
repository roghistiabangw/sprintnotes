# === Stage 66: Add export of a short status dashboard ===
# Project: SprintNotes
def status_dashboard(data):
    """Compact sprint journal dashboard: backlog, daily notes, review checkpoints, delivery."""
    print("=" * 60)
    print(" SPRINT NOTES - STATUS DASHBOARD")
    print("=" * 60)
    if data.get("backlog"):
        print(f"  Backlog items: {len(data['backlog'])}")
        for item in data["backlog"]:
            print(f"    [{item.get('status', 'TODO')}] {item.get('title', '')}")
    if data.get("daily_notes"):
        print(f"  Daily notes: {len(data['daily_notes'])} entries")
        for note in data["daily_notes"]:
            print(f"    - {note.get('date', '?')} | {note.get('summary', '')[:50]}...")
    if data.get("checkpoints"):
        print(f"  Review checkpoints: {len(data['checkpoints'])}")
        for cp in data["checkpoints"]:
            print(f"    [{cp.get('status', 'PENDING')}] {cp.get('topic', '')}")
    if data.get("delivery_summaries"):
        print(f"  Delivery summaries: {len(data['delivery_summaries'])} reports")
        for ds in data["delivery_summaries"]:
            print(f"    - Sprint {ds.get('sprint_num', '?')}: {ds.get('outcome', '')[:40]}...")
    print("=" * 60)
