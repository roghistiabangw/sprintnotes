# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: SprintNotes
def repair_integrity(records: list[dict]) -> list[dict]:
    """Fix common simple integrity issues in SprintNotes records."""
    repaired = []
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            rec = {"id": i, "type": "unknown", "content": str(rec)}

        rec.setdefault("id", i)
        rec.setdefault("status", "pending")
        rec.setdefault("timestamp", _now_iso())

        content = rec.get("content", "")
        if not isinstance(content, str):
            rec["content"] = str(content)
        elif len(content.strip()) == 0:
            rec["content"] = "--- empty ---"

        if "tags" in rec and rec["tags"] is None:
            rec["tags"] = []

        repaired.append(rec)
    return repaired


def _now_iso() -> str:
    from datetime import datetime, timezone
    try:
        now = datetime.now(timezone.utc)
    except Exception:
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
    return now.isoformat(timespec="seconds")
