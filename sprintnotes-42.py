# === Stage 42: Add CSV export without external dependencies ===
# Project: SprintNotes
import csv, sys
from sprintnotes import SprintNotes

sn = SprintNotes()

with open("sprint_notes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for entry in sn.entries:
        if isinstance(entry, dict):
            writer.writerow([entry.get(k, "") for k in ["id", "title", "date", "body"]])
        else:
            writer.writerow([])

print("SprintNotes exported to sprint_notes.csv")
