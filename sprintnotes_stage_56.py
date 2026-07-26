# === Stage 56: Add compact error classes for domain failures ===
# Project: SprintNotes
class SprintNotesError(Exception):
    """Base for all domain errors."""


class BacklogItemNotFound(SprintNotesError, KeyError):
    pass


class DailyNoteMissing(SprintNotesError, ValueError):
    pass


class ReviewCheckpointFailed(SprintNotesError):
    def __init__(self, task_id: str, expected: Any, actual: Any = None) -> None:
        super().__init__(f"Review for {task_id} failed.")
        self.task_id = task_id
        self.expected = expected
        self.actual = actual


class DeliverySummaryInvalid(SprintNotesError):
    pass
