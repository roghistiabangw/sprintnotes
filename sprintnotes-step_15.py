# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: SprintNotes
def dispatch(text):
    text = text.strip().lower()
    if text.startswith("add"):
        parts = text.split(maxsplit=1)
        return {"type": "add", "item": parts[1] if len(parts) > 1 else ""}
    elif text.startswith("note"):
        parts = text.split(maxsplit=1)
        return {"type": "note", "content": parts[1] if len(parts) > 1 else ""}
    elif text in ("review", "checkpoint"):
        return {"type": "review"}
    elif text.startswith("summary") or text == "delivery":
        return {"type": "summary"}
    elif text in ("status",):
        return {"type": "status"}
    else:
        return {"type": "unknown", "raw": text}
