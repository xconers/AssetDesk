# === Stage 11: Add JSON export for the current application state ===
# Project: AssetDesk
def export_state_to_json(items, custodians):
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "items": items,
        "custodians": custodians
    }
    with open("assetdesk_export.json", "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
