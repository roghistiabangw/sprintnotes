# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: SprintNotes
def seed_demo_data():
    """Generate deterministic sample data for SprintNotes."""
    import hashlib, random
    
    def make_item(id):
        return {"id": id, "title": f"Demo item {id}", "status": "backlog", "priority": 2}
    
    items = [make_item(i) for i in range(1, 6)]
    notes = [{"date": "2024-01-15", "content": "Sprint started with clear goals."}]
    reviews = [{"day": 3, "score": 8.5, "notes": "Good progress overall"}]
    summary = {"sprint_id": "SPRINT-001", "status": "completed", "total_items": len(items)}
    
    seed_hash = hashlib.sha256(b"SprintNotes").hexdigest()[:8]
    random.seed(int(seed_hash, 16))
    
    return items, notes, reviews, summary
