# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: AssetDesk
import json, os

def load_assets(path="assets.json"):
    try:
        with open(path) as f:
            data = json.load(f)
            if isinstance(data, list):
                return [Asset.from_dict(i) for i in data]
            raise ValueError("Root must be a list")
    except FileNotFoundError:
        print(f"[WARN] {path} not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {path}: {e}")
        return []
