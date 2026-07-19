# === Stage 32: Add pagination helpers for long console output ===
# Project: SprintNotes
def paged_print(items, page_size=15):
    """Print items in pages to console."""
    for i in range(0, len(items), page_size):
        chunk = items[i:i+page_size]
        print(f'--- Page {i//page_size + 1} ---')
        if not chunk:
            continue
        for item in chunk:
            print(' ' * (20 - len(str(i % page_size))) + str(item))
        print()

def clear_screen():
    """Clear console and return to start."""
    import os; os.system('cls' if os.name == 'nt' else 'clear')
