# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: AssetDesk
def validate_item_id(item_id):
    if not item_id:
        raise ValueError("Item ID cannot be empty")
    if len(item_id) > 20:
        raise ValueError("Item ID must be less than 20 characters")
    return True

def validate_custodian_name(name):
    if not name or len(name.strip()) < 3:
        raise ValueError("Custodian name is required and must be at least 3 characters")
    return True

def validate_due_date(date_str, today=None):
    from datetime import date, timedelta
    if today is None:
        today = date.today()
    try:
        d = date.fromisoformat(date_str)
        if d < today - timedelta(days=30):
            raise ValueError("Due date cannot be more than 30 days in the past")
        return True
    except (ValueError, TypeError):
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

def validate_condition_note(note):
    if note and len(note) > 500:
        raise ValueError("Condition note must be less than 500 characters")
    return True
