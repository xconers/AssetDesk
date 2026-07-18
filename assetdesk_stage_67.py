# === Stage 67: Add a function that returns key project metrics ===
# Project: AssetDesk
def project_metrics(items, custodians):
    """Return a dictionary of key AssetDesk metrics."""
    total_items = len(items)
    active_items = sum(1 for it in items if it.status == "checked_out")
    overdue_items = sum(
        1 for it in items
        if it.status == "checked_out" and it.due_date < datetime.now().date()
    )
    custodian_count = len(custodians)
    return {
        "total_items": total_items,
        "active_checkouts": active_items,
        "overdue_checkouts": overdue_items,
        "custodian_count": custodian_count,
    }
