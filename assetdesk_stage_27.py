# === Stage 27: Add monthly summary calculations ===
# Project: AssetDesk
def calculate_monthly_summary(items, custodians):
    from datetime import datetime
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    summary = {}
    for item in items:
        key = f"{item['custodian_id']}_{current_year}_{current_month}"
        if key not in summary:
            summary[key] = {'items': [], 'overdue_count': 0, 'total_value': 0}
        custodian_name = next((c['name'] for c in custodians if c['id'] == item['custodian_id']), f'Custodian {item["custodian_id"]}')
        summary[key]['items'].append({**item, 'custodian_name': custodian_name})
        summary[key]['total_value'] += float(item.get('value', 0))
        due_date = datetime.strptime(item['due_date'], '%Y-%m-%d')
        if due_date < now:
            summary[key]['overdue_count'] += 1
    return summary
