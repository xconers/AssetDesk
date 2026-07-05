# === Stage 31: Add compact table rendering for long lists ===
# Project: AssetDesk
def render_compact_table(items, max_rows=15):
    if len(items) > max_rows:
        items = items[:max_rows] + [f"... ({len(items)-max_rows} more)"]
    lines = ["ID\tName\tCustodian\tDue Date\tStatus", "-" * 40]
    for it in items:
        status = "Checked Out" if it.get("status") == "out" else "Available"
        due = it.get("due_date", "-").split("-")[2:] if isinstance(it.get("due_date"), str) and len(it["due_date"].split("-")) > 2 else "-"
        lines.append(f"{it['id']}\t{it['name'][:15]}\t{it['custodian'][:10]}\t{due}\t{status}")
    print("\n".join(lines))
