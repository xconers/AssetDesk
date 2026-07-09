# === Stage 43: Add CSV import for the primary record type ===
# Project: AssetDesk
import csv
from datetime import date, timedelta

def import_items(csv_path):
    items = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            item = {
                "id": row.get("id", ""),
                "name": row.get("name", ""),
                "category": row.get("category", ""),
                "status": row.get("status", ""),
                "custodian": row.get("custodian", ""),
                "due_date": date.fromisoformat(row["due_date"]),
                "condition_note": row.get("condition_note", ""),
            }
            items.append(item)
    return items

items = import_items("assets.csv")
print(f"Imported {len(items)} items.")
