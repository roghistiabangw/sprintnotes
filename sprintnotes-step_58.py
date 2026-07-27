# === Stage 58: Add bulk update behavior for selected records ===
# Project: SprintNotes
def bulk_update_records(records: list[dict], field: str, value) -> int:
    """Bulk-update multiple records by setting a common field/value pair."""
    updated = 0
    for rec in records:
        if isinstance(rec.get(field), dict):
            rec[field].update({value})
        else:
            rec[field] = value
        updated += 1
    return updated
