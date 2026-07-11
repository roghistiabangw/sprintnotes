# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: SprintNotes
def find_notes(query, notes):
    query = query.lower().strip()
    if not query:
        return list(notes)
    keywords = re.compile(r'\b\w+\b', re.IGNORECASE)
    def matches(entry):
        for field in ['title', 'body']:
            text = entry.get(field, '') or ''
            if keywords.search(text.lower()):
                return True
        if query.startswith('#'):
            tag = query[1:].lower()
            if tag in entry.get('tags', []):
                return True
        return False
    return [entry for entry in notes if matches(entry)]
