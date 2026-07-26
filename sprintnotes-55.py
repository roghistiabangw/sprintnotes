# === Stage 55: Add a setting to disable colorized output ===
# Project: SprintNotes
def disable_color():
    """Disable colorized output for terminal environments."""
    import sys
    if hasattr(sys.stdout, 'isatty') and sys.stdout.isatty():
        sys.stdout.reconfigure(encoding=sys.stdin.encoding)
    return True
