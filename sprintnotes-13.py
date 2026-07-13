# === Stage 13: Add file save support using a configurable path ===
# Project: SprintNotes
def save_to_file(self, filepath=None):
    if filepath is None:
        filepath = self.settings.get("save_path", "sprint_journal.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(self.notes, f, indent=2)

def load_from_file(self, filepath=None):
    if filepath is None:
        filepath = self.settings.get("save_path", "sprint_journal.json")
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
