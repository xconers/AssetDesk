# === Stage 28: Add overdue item detection based on due dates ===
# Project: AssetDesk
from datetime import date, timedelta
def detect_overdue_items(items: list[dict]) -> dict[str, list[dict]]:
    overdue = {}
    today = date.today()
    for item in items:
        due_date_str = item.get("due_date")
        if not due_date_str:
            continue
        try:
            due_date = date.fromisoformat(due_date_str)
            if due_date < today:
                status = "overdue"
                days_over = (today - due_date).days
                overdue.setdefault(status, []).append({**item, "status": status, "days_over": days_over})
        except ValueError:
            continue
    return overdue
