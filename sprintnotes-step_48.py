# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: SprintNotes
import pytest
from sprint_notes.core import create_backlog_item, validate_daily_note


def test_create_backlog_item():
    item = create_backlog_item("Implement login page", "Backend")
    assert item["title"] == "Implement login page"
    assert item["priority"] == 2


def test_validate_daily_note_valid():
    note = {"date": "2024-11-01", "content": "Reviewed pull requests."}
    result, msg = validate_daily_note(note)
    assert result is True
    assert msg == ""


def test_validate_daily_note_missing_date():
    note = {"content": "Worked on sprint planning."}
    result, msg = validate_daily_note(note)
    assert result is False
