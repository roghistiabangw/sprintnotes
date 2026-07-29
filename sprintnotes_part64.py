# === Stage 64: Add validation for relationship references ===
# Project: SprintNotes
import os

def validate_references(sprint_data, ref_file="references.txt"):
    """Validate that all relationship references in sprint data exist."""
    if not isinstance(sprint_data, dict):
        raise ValueError("sprint_data must be a dictionary")
    
    valid_refs = set()
    try:
        with open(ref_file) as f:
            for line in f:
                line = line.strip().lower()
                if line and not line.startswith("#"):
                    valid_refs.add(line)
    except FileNotFoundError:
        pass
    
    errors = []
    
    for sprint_type, items in sprint_data.items():
        if not isinstance(items, list):
            raise ValueError(f"{sprint_type} must be a list")
        
        for item in items:
            if not isinstance(item, dict):
                raise ValueError("Each item must be a dictionary")
            
            relationships = item.get("relationships", [])
            if not isinstance(relationships, list):
                raise ValueError(f"Relationships in {sprint_type} must be a list")
            
            for rel in relationships:
                if not isinstance(rel, dict):
                    raise ValueError("Each relationship must be a dictionary")
                
                ref_id = rel.get("reference_id", "")
                if ref_id and ref_id.lower() not in valid_refs:
                    errors.append(f"Invalid reference '{ref_id}' in {sprint_type}")
    
    return errors

# Example usage
if __name__ == "__main__":
    sprint_data = {
        "backlog_items": [
            {"id": 1, "title": "Feature A", "relationships": [{"reference_id": "user-1"}]},
            {"id": 2, "title": "Bug Fix B", "relationships": [{"reference_id": "nonexistent"}]}
        ],
        "daily_notes": [
            {"date": "2024-01-01", "note": "Sprint started", "relationships": []}
        ]
    }
    
    errors = validate_references(sprint_data)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("All references are valid!")
