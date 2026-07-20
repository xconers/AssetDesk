# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: AssetDesk
def build_validation_report(checkout_log):
    warnings = []
    errors = []
    for entry in checkout_log:
        if entry.get("due_date") and entry["due_date"] < datetime.now():
            errors.append(f"Overdue: {entry['item_name']} returned to {entry['custodian_email']} on {entry['return_date']}, due was {entry['due_date'].strftime('%Y-%m-%d')}.")
        if not entry.get("condition_note"):
            warnings.append(f"No condition note recorded for return of {entry['item_name']} by {entry['custodian_email']} at {entry['return_date']}.")
        if entry.get("status") != "returned":
            warnings.append(f"Checkout still open: {entry['item_name']} was not returned or lost.")
    report = {"warnings": warnings, "errors": errors}
    return report
