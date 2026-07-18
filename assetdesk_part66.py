# === Stage 66: Add export of a short status dashboard ===
# Project: AssetDesk
def dashboard(items, custodians):
    due = sum(1 for i in items if i["due_date"] and (i["due_date"] < "2026-05-31"))
    overdue = sum(1 for i in items if i.get("condition_note", "").lower() == "damaged")
    checked_out = sum(1 for i in items if not i["returned"])
    total, unique = len(items), len(set(i["custodian"] for i in items))
    print(f"Total: {total} | Unique custodians: {unique} | Checked out: {checked_out}")
    print(f"Due soon (by 2026-05-31): {due} | Damaged/returned: {overdue}")
