# === Stage 40: Add plain text report export ===
# Project: AssetDesk
def export_report_txt(records):
    """Export asset records as a plain text report."""
    out = []
    out.append("=" * 60)
    out.append("ASSETDESK CHECKOUT REPORT")
    out.append("=" * 60)
    if not records:
        out.append("(no records to export)")
        return "\n".join(out)
    for r in records:
        out.append(f"Item: {r['item']} | Owner: {r['custodian']}")
        out.append(f"Due: {r['due_date']} | Status: {'Overdue' if r['returned'] else 'Active'}")
        note = r.get('condition_note', '') or ''
        if note:
            out.append(f"Note: {note}")
        out.append("-" * 40)
    return "\n".join(out)
