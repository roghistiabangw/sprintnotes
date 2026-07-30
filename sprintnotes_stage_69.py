# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: SprintNotes
def reset_demo_data():
    """Reset all SprintNotes demo data to a clean state for manual testing."""
    import json, os, shutil

    DATA_FILE = "sprint_notes.json"
    BACKUP_DIR = "backups"

    if not os.path.exists(DATA_FILE):
        print("No existing data file found. Starting fresh.")
        return

    # Create backup directory and copy current data
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}.json")
    shutil.copy2(DATA_FILE, backup_path)
    print(f"Backup saved to {backup_path}")

    # Clear all sprint data
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "sprints": [],
            "backlog": [],
            "daily_notes": {},
            "checkpoints": [],
            "summaries": []
        }, f, indent=2)

    print("SprintNotes data has been reset successfully!")
    print(f"Original data backed up to {backup_path}")

if __name__ == "__main__":
    reset_demo_data()
