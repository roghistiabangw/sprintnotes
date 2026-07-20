# === Stage 34: Add support for multiple local user profiles ===
# Project: SprintNotes
class UserProfiles:
    def __init__(self):
        self.profiles = {}
    
    def load(self, filepath='profiles.json'):
        import json
        with open(filepath) as f:
            data = json.load(f)
            for name in data:
                self.profiles[name] = data[name]
    
    def save(self, filepath='profiles.json'):
        import json
        with open(filepath, 'w') as f:
            json.dump(list(self.profiles.values()), f)
    
    def add_profile(self, name, sprint_id, notes):
        if name not in self.profiles:
            self.profiles[name] = {'sprint_id': sprint_id, 'notes': []}
        self.profiles[name]['notes'].append(notes)
    
    def get_notes(self, name):
        return self.profiles.get(name, {}).get('notes', [])
