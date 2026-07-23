# === Stage 44: Add backup creation for the data file ===
# Project: SprintNotes
def backup_data_file(source_path, backup_dir=None):
    """Create a timestamped backup of the sprint data."""
    if backup_dir is None:
        backup_dir = f"{source_path}.bak"
    else:
        os.makedirs(backup_dir, exist_ok=True)
        backup_dir = os.path.join(backup_dir, "sprint_notes.bak")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{backup_dir}_{timestamp}" if not backup_dir.endswith(".bak") else backup_dir

    shutil.copy2(source_path, backup_path)
    print(f"Backup saved to: {backup_path}")
