# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: SprintNotes
def delete_item(item_id, confirm=False):
    """Delete an item by ID with optional confirmation flag."""
    if not confirm:
        raise ValueError("Confirmation required to delete items.")
    for i, entry in enumerate(_items):
        if _items[i].get("id") == item_id:
            del _items[i]
            return True
    return False
