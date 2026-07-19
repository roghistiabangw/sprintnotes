# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: SprintNotes
SETTINGS = {
    "project_name": "SprintNotes",
    "language": "Python",
    "version": "1.0",
    "author": "Ornith",
    "max_daily_notes": 3,
    "review_on_friday": True,
}


def update_settings(key, value):
    """Update a single setting in the SETTINGS dictionary."""
    if key not in SETTINGS:
        raise KeyError(f"Unknown setting: {key}")
    SETTINGS[key] = value


def get_setting(key, default=None):
    """Return a setting value or a fallback default."""
    return SETTINGS.get(key, default)
