# === Stage 43: Add CSV import for the primary record type ===
# Project: SprintNotes
def import_backlog_from_csv(csv_path):
    """Import backlog items from a CSV with columns: id,title,description,status,priority."""
    import csv
    items = []
    try:
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = {
                    'id': int(row['id']),
                    'title': row['title'].strip(),
                    'description': row['description'].strip() if row.get('description') else '',
                    'status': row['status'].strip().lower(),
                    'priority': row['priority'].strip().upper() or 'medium',
                }
                items.append(item)
    except FileNotFoundError:
        print(f"CSV file not found: {csv_path}")
    return items
