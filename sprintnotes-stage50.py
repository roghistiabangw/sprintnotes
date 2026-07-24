# === Stage 50: Add unit tests for import and export behavior ===
# Project: SprintNotes
import io
from sprintnotes.core import SprintNotebook, DailyNote, BacklogItem, ReviewCheckpoint, DeliverySummary


def _serialize(obj):
    buf = io.StringIO()
    SprintNotebook._write_json(buf, obj) if hasattr(SprintNotebook, '_write_json') else SprintNotebook.write_json(obj, buf)
    return buf.getvalue()


class TestImportExport:
    def test_import_export_roundtrip(self):
        notebook = SprintNotebook("Sprint 1")
        item = BacklogItem("login", "Implement login page", None, False)
        note = DailyNote(2023, 6, 15, "Started login module")
        checkpoint = ReviewCheckpoint("Login flow", ["Login UI", "Auth API"], True)
        summary = DeliverySummary("Sprint 1", [item], [note], checkpoint)

        notebook.add_backlog_item(item)
        notebook.add_daily_note(note)
        notebook.add_checkpoint(checkpoint)
        notebook.add_summary(summary)

        serialized = _serialize(notebook)
        restored = SprintNotebook.from_json(serialized)
        assert len(restored.backlog_items) == 1
        assert len(restored.daily_notes) == 1
        assert len(restored.checkpoints) == 1
        assert len(restored.summaries) == 1

    def test_import_export_from_dict(self):
        data = {
            "name": "Sprint 2",
            "backlog_items": [{"title": "dashboard", "description": "Dashboard", "priority": None, "done": False}],
            "daily_notes": [],
            "checkpoints": [],
            "summaries": []
        }
        notebook = SprintNotebook.from_json(data)
        assert notebook.name == "Sprint 2"
