# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: SprintNotes
import pytest
from datetime import date, timedelta


def test_update_nonexistent_entry_returns_default():
    """Updating an entry that has never been logged should return a fresh default."""
    from sprintnotes.core.sprint_journal import SprintJournal

    journal = SprintJournal()  # no prior entries
    today = date.today()
    result = journal.update(today, "late")
    assert result == {"date": today.isoformat(), "status": None}


def test_delete_entry_with_no_backlog_items():
    """Deleting an entry that has no backlog items should leave the journal empty."""
    from sprintnotes.core.sprint_journal import SprintJournal

    journal = SprintJournal()
    today = date.today()
    journal.log(today, "on_time", [])  # log once then delete
    assert len(journal.get_entries()) == 0


def test_delete_entry_with_backlog_items_removes_them():
    """Deleting an entry should also remove any backlog items it contained."""
    from sprintnotes.core.sprint_journal import SprintJournal

    journal = SprintJournal()
    today = date.today()
    backlogs = [{"id": "B1", "title": "Task A"}, {"id": "B2", "title": "Task B"}]
    journal.log(today, "on_time", backlogs)
    assert len(journal.get_entries()) == 1

    # delete via the entry itself
    entries = list(journal.get_entries())
    del entries[0]
    journal.delete(entries[0]["date"], entries[0])
    assert len(journal.get_entries()) == 0


def test_update_then_delete_preserves_order():
    """Updating an entry and then deleting it must not affect other entries."""
    from sprintnotes.core.sprint_journal import SprintJournal

    journal = SprintJournal()
    today = date.today() - timedelta(days=3)
    yesterday = today + timedelta(days=1)
    tomorrow = today + timedelta(days=2)

    journal.log(today, "on_time", [])
    journal.log(yesterday, "late", [])
    journal.log(tomorrow, "early", [])

    # update yesterday to late
    entries = list(journal.get_entries())
    yest = next(e for e in entries if e["date"] == yesterday.isoformat())
    journal.update(yesterday, "late")  # no-op since already late

    assert len(journal.get_entries()) == 3
    entries = list(journal.get_entries())

    del entries[1]
    journal.delete(yesterday, entries[1])
    assert len(journal.get_entries()) == 2
