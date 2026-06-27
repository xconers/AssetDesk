# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: AssetDesk
def format_item(item):
    status = "CHECKED OUT" if item.checked_out else "AVAILABLE"
    due_str = f"Due: {item.due_date}" if item.checked_out else ""
    notes = f"\nCondition: {item.condition_note}" if item.condition_note else ""
    return (f"[{status}] {item.name}\n"
            f"Custodian: {item.custodian_name}{due_str}\n" + notes)

def format_audit_report(items, custodians):
    total = len(items)
    checked_out = sum(1 for i in items if i.checked_out)
    available = total - checked_out
    overdue = [i.name for i in items if i.checked_out and datetime.datetime.now() > datetime.datetime.strptime(i.due_date, "%Y-%m-%d")]
    report_lines = ["=== ASSET AUDIT REPORT ===", f"Total Items: {total}", f"Available: {available}", f"Checked Out: {checked_out}"]
    if overdue:
        report_lines.append(f"\nOVERDUE ITEMS:")
        for name in overdue:
            report_lines.append(f"- {name}")
    else:
        report_lines.append("\nNo overdue items.")
    return "\n".join(report_lines)
