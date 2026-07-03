# === Stage 26: Add weekly summary calculations ===
# Project: AssetDesk
def generate_weekly_summary(items, custodians):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    overdue_count = 0
    late_returns = []
    upcoming_due = []
    
    for item in items:
        due_date = item['due_date']
        custodian_name = custodians.get(item['custodian_id'], 'Unknown')
        
        if due_date < today:
            overdue_count += 1
            late_returns.append({
                "item": item["name"],
                "custodian": custodian_name,
                "days_overdue": (today - due_date).days
            })
        elif week_start <= due_date <= week_end and not item['returned']:
            upcoming_due.append({
                "item": item["name"],
                "custodian": custodian_name,
                "due_date": due_date.strftime("%Y-%m-%d")
            })
    
    summary = {
        "report_period": f"{week_start} to {week_end}",
        "total_overdue_items": overdue_count,
        "late_return_details": late_returns[:5],  # Limit for readability
        "upcoming_due_this_week": upcoming_due
    }
    
    return summary
