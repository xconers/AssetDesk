# === Stage 37: Add recommendations for the next useful action ===
# Project: AssetDesk
def recommend_next_action(asset):
    """Suggest a useful next step based on asset state."""
    if asset["status"] == "checked_out" and asset.get("due_date"):
        remaining = (datetime.date.today() - datetime.date.fromisoformat(asset["due_date"])).days
        if remaining <= 3:
            return f"⚠️ Return '{asset['name']}' soon — due in {remaining} days!"
    elif asset["status"] == "checked_out":
        custodian = asset.get("custodian", {}).get("display_name", "Unknown")
        return f"📋 Confirm with {custodian} whether '{asset['name']}' is still needed."
    if not asset.get("condition_note"):
        return f"✏️ Add a condition note for '{asset['name']}' before returning it."
    if asset["status"] == "checked_in":
        notes = asset.get("checkin_notes", {})
        if "damaged" in notes:
            return f"🔧 Schedule maintenance for '{asset['name']}' — reported damaged."
        return f"✅ '{asset['name']}' is back. Consider filing a brief post-check-in log."
    return ""
