# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: AssetDesk
from datetime import datetime, timedelta
import re

def parse_due_date(date_str: str) -> tuple[datetime | None, str]:
    """Parse date strings with flexible formats and return (parsed_date, error_message)."""
    if not date_str or date_str.strip() == "":
        return None, "Empty date string provided."
    
    patterns = [
        ("%Y-%m-%d", "%Y/%m/%d"),  # 2023-10-25 or 2023/10/25
        ("%B %d, %Y", "%b. %d, %Y"),  # October 25, 2023 or Oct. 25, 2023
        ("%d.%m.%Y", None),  # 25.10.2023 (European)
    ]
    
    for fmt, alt_fmt in patterns:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt, ""
        except ValueError:
            if alt_fmt and date_str.strip() != "":
                try:
                    dt = datetime.strptime(date_str.strip(), alt_fmt)
                    return dt, ""
                except ValueError:
                    continue
    
    # Attempt regex for loose matching (e.g., 25/10/23 or Oct-25)
    match = re.match(r"(\w{3}|\d{1,2})[-/.](\d{1,2})(?:[-/.]?)?(\d{2,4})", date_str.strip())
    if match:
        month_str, day, year = match.groups()
        try:
            # Normalize short months
            month_map = {
                "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
            }
            month = month_map.get(month_str.capitalize(), int(month_str))
            year = int(year) if len(year) == 4 else datetime.now().year
            
            # Handle ambiguous day/month order for short years (assume DD/MM/YY if MM > 12 impossible)
            dt_attempt = datetime(year, month, int(day))
            return dt_attempt, ""
        except ValueError:
            pass
    
    return None, f"Unable to parse date string: '{date_str}'."

def calculate_overdue_days(due_date_str: str | None, today: datetime | None = None) -> tuple[int | None, str]:
    """Calculate overdue days. Returns (days_overdue, error_message)."""
    if not due_date_str or today is None:
        return 0, "Missing date inputs for calculation."
    
    parsed_dt, err_msg = parse_due_date(due_date_str)
    if err_msg:
        return -1, f"Date parsing failed: {err_msg}"
    
    if parsed_dt > today:
        return None, "Asset is not yet due."
