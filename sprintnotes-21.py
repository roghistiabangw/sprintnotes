# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: SprintNotes
def archive_records(records, target_dir=".archive", prefix="sprint_"):
    """Compact: move completed/old records to an on-disk directory."""
    import shutil, os, datetime
    today = datetime.date.today().strftime("%Y%m%d")
    for rec in records:
        if getattr(rec, "completed", False) or rec.get("date", "") < today:
            fname = prefix + str(getattr(rec, "id", hash(str(rec))) % 10**4).zfill(4) + ".json"
            dst = os.path.join(target_dir, today, fname)
            shutil.move(str(rec), dst)
    return target_dir
