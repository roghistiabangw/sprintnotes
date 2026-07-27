# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: SprintNotes
def bulk_delete(self, ids: list[str], confirm: bool = False) -> int:
        """Delete multiple records only when a confirmation flag is set."""
        if not confirm and len(ids) > 1:
            raise PermissionError(
                f"bulk_delete requires confirm=True for {len(ids)} items; "
                f"pass confirm=True or delete one at a time."
            )
        count = 0
        for rid in ids:
            rec = self.get_by_id(rid)
            if rec is None:
                raise KeyError(f"No record with id={rid!r}")
            rec.delete()
            count += 1
        return count
