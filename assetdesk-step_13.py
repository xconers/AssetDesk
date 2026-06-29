# === Stage 13: Add file save support using a configurable path ===
# Project: AssetDesk
import os, json, datetime
from pathlib import Path

def save_asset(asset: dict) -> None:
    """Persist asset data to a configurable JSON file."""
    config = get_config()
    path = Path(config.get("storage_path", "assets.json"))
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asset, f, indent=2)
    except IOError as e:
        print(f"Failed to save asset: {e}")

def get_config() -> dict:
    """Load configuration from environment or default."""
    config = {"storage_path": "assets.json"}
    if os.path.exists("config.env"):
        for line in open("config.env").readlines():
            key, val = line.strip().split("=")
            config[key] = val
    return config

def load_assets() -> list:
    """Load all assets from the configured storage path."""
    config = get_config()
    path = Path(config.get("storage_path", "assets.json"))
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else [data]
    except (IOError, json.JSONDecodeError):
        return []
