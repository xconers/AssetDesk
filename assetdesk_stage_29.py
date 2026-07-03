# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: AssetDesk
from datetime import datetime, timedelta
def get_upcoming_items(items: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    upcoming = []
    for item in items:
        due_date_str = item.get("due_date") or ""
        if not due_date_str:
            continue
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            if now <= due_date <= cutoff and item.get("status") == "checked_out":
                upcoming.append({**item, "days_left": (due_date - now).days})
        except ValueError:
            continue
    return sorted(upcoming, key=lambda x: x["due_date"])
