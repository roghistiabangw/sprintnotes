# === Stage 41: Add plain text import for a simple line-based format ===
# Project: SprintNotes
def parse_plain(text: str) -> list[dict]:
    """Read a line-based sprint journal, splitting each entry on blank lines."""
    entries = []
    current = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            if current:
                entries.append(current)
                current = {}
        else:
            key, _, value = stripped.partition(":")
            if value and value != "<empty>":
                current[key] = value
    if current:
        entries.append(current)
    return entries
