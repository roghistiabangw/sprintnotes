# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: SprintNotes
def import_json(path):
    """Load a JSON file, returning a dict/list and raising a clear error on malformed data."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"SprintNotes data not found at {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Malformed JSON in {path}: {exc.msg} at line {exc.lineno}, column {exc.colno}"
        ) from exc
    except PermissionError:
        raise PermissionError(f"No permission to read {path}") from None
