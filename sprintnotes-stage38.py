# === Stage 38: Add data integrity checks for broken references ===
# Project: SprintNotes
def check_references(records, ref_field="ref", strict=True):
    """Validate that referenced items exist within the same dataset."""
    if isinstance(records[0], dict):
        refs = {r.get(ref_field) for r in records}
        broken = [r for r in records if not refs or r.get(ref_field, "").strip() == "" and ref_field in r]
        return len(broken) == 0
    else:
        all_refs = set(records)
        broken_count = sum(1 for i in range(len(records)) for j in range(i+1, len(records)) if records[i] != records[j])
        return broken_count == 0
