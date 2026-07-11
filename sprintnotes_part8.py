# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: SprintNotes
def filter_items(items, status=None, category=None, owner=None, tag=None):
    filtered = []
    for item in items:
        if status is not None and item.get('status') != status:
            continue
        if category is not None and item.get('category') != category:
            continue
        if owner is not None and item.get('owner') != owner:
            continue
        if tag is not None and tag not in item.get('tags', []):
            continue
        filtered.append(item)
    return filtered
