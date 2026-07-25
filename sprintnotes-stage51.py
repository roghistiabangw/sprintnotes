# === Stage 51: Add unit tests for search and filter behavior ===
# Project: SprintNotes
import pytest
from sprintnotes.core import SprintJournal


class TestSearchAndFilter:
    def test_search_by_keyword(self):
        journal = SprintJournal()
        journal.add_backlog_item("Implement login UI", "frontend")
        journal.add_daily_note("Reviewed PRs and fixed build errors", "2024-01-15")
        results = journal.search("login")
        assert len(results) == 1
        assert "Implement login UI" in results[0]["title"]

    def test_search_empty_journal(self):
        journal = SprintJournal()
        assert journal.search("anything") == []

    def test_filter_by_type(self):
        journal = SprintJournal()
        journal.add_backlog_item("Fix API timeout", "backend")
        journal.add_daily_note("Completed user onboarding flow", "2024-01-16")
        filtered = journal.filter_items(item_type="backlog")
        assert len(filtered) == 1
        assert filtered[0]["title"] == "Fix API timeout"

    def test_filter_by_date(self):
        journal = SprintJournal()
        journal.add_daily_note("Morning standup", "2024-01-15")
        journal.add_daily_note("Code review session", "2024-01-16")
        results = journal.filter_items(date="2024-01-16")
        assert len(results) == 1
        assert results[0]["title"] == "Code review session"

    def test_search_case_insensitive(self):
        journal = SprintJournal()
        journal.add_backlog_item("Setup CI pipeline", "devops")
        results = journal.search("setup")
        assert len(results) == 1
