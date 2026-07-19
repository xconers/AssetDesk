# === Stage 72: Add Markdown report export ===
# Project: AssetDesk
def export_markdown_report(records, output_path):
    """Export current checkout records to a formatted Markdown report."""
    lines = ["# AssetDesk Audit Report", "", "---"]
    
    # Header row
    lines.append("| Item | Custodian | Due Date | Condition Notes | Status |")
    lines.append("|------|-----------|----------|-----------------|--------|")

    for rec in records:
        item_name = rec.get("item_name", "N/A")
        custodian = rec.get("custodian", "Unknown")
        due_date = rec.get("due_date", "")
        condition_notes = rec.get("condition_notes", "")
        
        status = "Active" if not rec.get("returned", False) else "Returned"
        note_badge = f":warning: {condition_notes}" if condition_notes else ""

        lines.append(f"| {item_name} | {custodian} | {due_date} | {note_badge} | {status} |")

    # Summary section
    active_count = sum(1 for r in records if not r.get("returned", False))
    returned_count = sum(1 for r in records if r.get("returned", False))
    
    lines.append("\n## Summary\n")
    lines.append(f"- **Active Checkouts**: {active_count}")
    lines.append(f"- **Returned Items**: {returned_count}")
    lines.append(f"- **Total Records**: {len(records)}\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    return output_path
