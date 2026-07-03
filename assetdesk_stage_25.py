# === Stage 25: Add daily summary calculations ===
# Project: AssetDesk
def calculate_daily_summary(items, custodians):
    from datetime import date, timedelta
    today = date.today()
    summary = {d: {'checked_out': 0, 'overdue': 0} for d in [today, today - timedelta(days=1), today - timedelta(days=2)]}
    
    def is_overdue(item):
        if item['custodian'] not in custodians or item.get('status') != 'checked_out':
            return False
        due = date.fromisoformat(item['due_date'])
        return due < today
    
    for item in items:
        if item['custodian'] in custodians and item.get('status') == 'checked_out':
            summary[today]['checked_out'] += 1
            if is_overdue(item):
                summary[today]['overdue'] += 1
            elif date.fromisoformat(item['due_date']) < today - timedelta(days=2):
                summary[today - timedelta(days=1)]['checked_out'] += 1
    
    return {k.strftime('%Y-%m-%d'): v for k, v in sorted(summary.items())}
