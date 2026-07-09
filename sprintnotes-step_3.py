# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: SprintNotes
import re

def validate_id(value, label):
    if not value:
        raise ValueError(f"{label} is required")
    return bool(re.match(r"^[A-Za-z0-9_-]{1,32}$", value.strip()))

def validate_short_text(value, max_len=80, min_len=1):
    v = (value or "").strip()
    if not v:
        raise ValueError(f"{label} is required")
    if len(v) > max_len:
        raise ValueError(f"{label} exceeds {max_len} chars")
    return v

def validate_date(value, fmt="%Y-%m-%d"):
    try:
        return datetime.strptime(value.strip(), fmt)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid date format. Use {fmt}")
