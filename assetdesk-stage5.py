# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: AssetDesk
def update_asset(asset_id: int, **kwargs) -> dict:
    if asset_id not in assets_db:
        return {"status": "error", "message": f"Asset {asset_id} not found"}
    
    existing = assets_db[asset_id].copy()
    for key, value in kwargs.items():
        if key in existing and value is not None:
            existing[key] = value
    
    # Validate condition notes format before saving
    if "condition_notes" in kwargs and isinstance(kwargs["condition_notes"], str):
        existing["condition_notes"] = f"[{kwargs['condition_notes']}]".strip()

    assets_db[asset_id] = existing
    return {"status": "success", "data": existing}
