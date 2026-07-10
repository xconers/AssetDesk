# === Stage 45: Add restore from backup with validation ===
# Project: AssetDesk
def restore_from_backup(backup_path):
    """Restore AssetDesk data from a backup JSON file with basic validation."""
    import os, json
    
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    
    try:
        with open(backup_path) as f:
            backup_data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        raise ValueError(f"Invalid or unreadable backup file: {e}")
    
    required_keys = {"items", "custodians"}
    if not all(key in backup_data for key in required_keys):
        raise ValueError("Backup missing required keys: items and custodians")
    
    try:
        data["items"].extend(backup_data["items"])
        existing_ids = {item["id"] for item in data["items"]}
        new_items = [item for item in backup_data["items"] if item["id"] not in existing_ids]
        data["items"].extend(new_items)
        
        custodians_in_backup = set(custodian["name"] for custodian in backup_data.get("custodians", []))
        custodians_in_data = {c["name"] for c in data["custodians"]}
        new_custodians = [c for c in backup_data["custodians"] if c["name"] not in custodians_in_data]
        data["custodians"].extend(new_custodians)
    except KeyError as e:
        raise ValueError(f"Unexpected structure in backup data: {e}")
    
    print(f"Restored from backup: added {len(new_items)} items, {len(new_custodians)} custodians")
