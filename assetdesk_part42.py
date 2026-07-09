# === Stage 42: Add CSV export without external dependencies ===
# Project: AssetDesk
import csv, io


def export_to_csv(items):
    """Export asset items to a CSV string without external dependencies."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["item_id", "name", "custodian", "due_date", "condition_note"])
    for item in items:
        writer.writerow([
            item.get("item_id", ""),
            item.get("name", ""),
            item.get("custodian", ""),
            item.get("due_date", ""),
            item.get("condition_note", ""),
        ])
    return output.getvalue()
