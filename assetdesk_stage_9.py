# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: AssetDesk
def sort_assets(key="last_update"):
    """Sort assets by title, date, priority, or last update."""
    order = {"title": 0, "due_date": 1, "priority": 2, "last_update": 3}
    if key not in order: raise ValueError(f"Unknown sort key: {key}")
    reverse = (key == "priority") and ("high" in str(getattr(asset, 'status', '')))
    return sorted(assets, key=lambda x: getattr(x, key) or "", reverse=reverse)
