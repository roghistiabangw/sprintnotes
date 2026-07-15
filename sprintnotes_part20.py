# === Stage 20: Add duplicate detection for newly created records ===
# Project: SprintNotes
def _has_duplicate(sprint, record):
    if sprint is None:
        return False
    same_type = type(record) == type(sprint._last_record)
    if not same_type or sprint._last_record is None:
        return False
    key_field = {
        BacklogItem: 'title',
        DailyNote: 'date',
        ReviewCheckpoint: 'name',
        DeliverySummary: 'sprint_name',
    }.get(same_type, None)
    if key_field is None:
        return False
    return getattr(record, key_field) == getattr(sprint._last_record, key_field)

def _check_duplicates(self):
    self._last_record = None
    for sprint in self.sprints.values():
        r = sprint._last_record
        if r is not None:
            self._last_records.append(r)
    return self._last_records
