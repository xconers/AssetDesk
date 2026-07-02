# === Stage 24: Add grouped summaries by category or status ===
# Project: AssetDesk
def generate_grouped_summary(items, group_by='category'):
    from collections import defaultdict
    groups = defaultdict(list)
    for item in items:
        key = item.get(group_by, 'Unknown') or 'Unknown'
        groups[key].append(item)
    
    report_lines = ["=== Asset Summary by Category ===", ""]
    for category, group_items in sorted(groups.items()):
        total_count = len(group_items)
        overdue = sum(1 for i in group_items if (i.get('due_date') or '9999-12-31') < get_today())
        report_lines.append(f"[{category}] {total_count} items | Overdue: {overdue}")
    
    return "\n".join(report_lines)
