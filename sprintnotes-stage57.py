# === Stage 57: Add structured result objects for command handlers ===
# Project: SprintNotes
class SprintResult:
    """Structured result for sprint command handlers."""

    def __init__(self, status: str = "ok", message: str = "", data=None):
        self.status = status
        self.message = message
        self.data = data or {}

    @property
    def success(self) -> bool:
        return self.status == "ok"

    def to_dict(self) -> dict:
        result = {"status": self.status, "message": self.message}
        if self.data is not None:
            result["data"] = self.data
        return result

    def __repr__(self):
        return f"SprintResult(status={self.status!r}, message={self.message!r})"
