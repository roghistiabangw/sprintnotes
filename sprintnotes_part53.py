# === Stage 53: Add command help text and usage examples ===
# Project: SprintNotes
def show_help():
    """Print usage information and examples for SprintNotes."""
    print("SprintNotes — a compact sprint journal")
    print()
    print("Usage:")
    print("  python sprintnotes.py add-item <title> [--points N]")
    print("  python sprintnotes.py daily-note <date>")
    print("  python sprintnotes.py checkpoint [--name Review1]")
    print("  python sprintnotes.py summary")
    print()
    print("Examples:")
    print('  python sprintnotes.py add-item "Fix login bug" --points 3')
    print('  python sprintnotes.py daily-note 2025-07-15')
    print('  python sprintnotes.py checkpoint --name Review1')
    print("  python sprintnotes.py summary")
