# === Stage 45: Add restore from backup with validation ===
# Project: SprintNotes
def restore_backup(backup_path, target_dir):
    """Restore a JSON backup with validation and log errors."""
    import json, os, shutil
    if not os.path.isfile(backup_path):
        print(f"Backup file not found: {backup_path}")
        return False
    try:
        with open(backup_path) as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to read backup JSON: {e}")
        return False
    if not isinstance(data, list):
        print("Backup must be a JSON array of records")
        return False
    for i, rec in enumerate(data):
        if not isinstance(rec, dict) or 'id' not in rec:
            print(f"Record {i} is invalid (missing id field)")
            continue
        shutil.rmtree(target_dir, ignore_errors=True)
        try:
            with open(os.path.join(target_dir, f"{rec['id']}.json"), "w") as out:
                json.dump(rec, out, indent=2)
        except Exception as e:
            print(f"Failed to write record {rec.get('id')}: {e}")
    print(f"Restored {len(data)} records to {target_dir}")
    return True
