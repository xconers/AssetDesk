# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: AssetDesk
def format_due_date(due):
    """Return a human-readable due date string, or 'Overdue' if past."""
    from datetime import datetime, timedelta
    now = datetime.now()
    if due and due < now:
        return "Overdue"
    if not due:
        return "No due date"
    return due.strftime("%B %d, %Y")

def summarize_audit(entries):
    """Summarize audit entries into a short status report."""
    overdue = [e for e in entries if e.get("status") == "overdue"]
    returned = [e for e in entries if e.get("status") == "returned"]
    return {
        "total": len(entries),
        "returned": len(returned),
        "overdue": len(overdue),
        "active": len(entries) - len(returned) - len(overdue),
    }

def validate_due_date(due):
    """Validate that a due date is in the future or None."""
    if due is not None:
        from datetime import datetime, timedelta
        now = datetime.now() + timedelta(days=1)  # allow same-day returns
        return due >= now
    return True

def parse_condition_note(note):
    """Parse a condition note into structured fields."""
    if not note:
        return {"condition": "unknown", "severity": None, "message": ""}
    parts = note.split("|")
    return {
        "condition": parts[0].strip().lower() if len(parts) > 0 else "unknown",
        "severity": parts[1].strip() if len(parts) > 1 else None,
        "message": parts[2].strip() if len(parts) > 2 else note,
    }

def generate_due_date_reminder(due):
    """Generate a reminder message for upcoming due dates."""
    from datetime import datetime, timedelta
    if not due:
        return None
    days_left = (due - datetime.now()).days
    if days_left <= 0:
        return f"OVERDUE: Item must be returned by {due.strftime('%Y-%m-%d')}"
    elif days_left == 1:
        return "TOMORROW: Item is due for return"
    else:
        return f"DUE IN {days_left} DAYS: Reminder to return item on {due.strftime('%Y-%m-%d')}"
