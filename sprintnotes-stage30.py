# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: SprintNotes
def parse_date(s, formats=("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y", "%Y%m%d")):
    """Parse a date string and return a datetime.date object."""
    if not s or not isinstance(s, str):
        raise ValueError("Date string must be a non-empty string.")
    s = s.strip()
    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(s, fmt)
            return dt.date()
        except ValueError:
            continue
    raise ValueError(f"Could not parse date '{s}'. Expected format like YYYY-MM-DD.")


def today():
    """Return today's date as a date object."""
    return datetime.date.today()


def is_valid_date(s):
    """Check whether the string represents a valid date; returns True or False."""
    try:
        parse_date(s)
        return True
    except ValueError:
        return False
