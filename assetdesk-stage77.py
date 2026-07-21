# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: AssetDesk
def format_due_date(due: datetime.date) -> str:
    """Return a formatted due date string."""
    return due.strftime("%Y-%m-%d")

def validate_custodian_email(email: str, custodians: dict[str, Custodian]) -> bool:
    """Check if the email belongs to an existing custodian."""
    for _, c in custodians.items():
        if c.email == email:
            return True
    return False

def generate_audit_summary(items: list[Asset], due_limit: int = 30) -> str:
    """Generate a brief audit summary of overdue items."""
    overdue = [f for f in items if f.due_date and f.due_date < datetime.date.today() and not f.checked_out]
    return f"Audit Summary: {len(overdue)} item(s) are currently overdue."

def calculate_age_days(due: datetime.date, checkout: datetime.date | None = None) -> int:
    """Calculate the number of days since due date."""
    if checkout is None:
        checkout = datetime.date.today()
    return (checkout - due).days
