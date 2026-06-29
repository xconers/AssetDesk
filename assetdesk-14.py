# === Stage 14: Add file load support with fallback demo data ===
# Project: AssetDesk
import json, os
from pathlib import Path

def load_or_demo(items_path: str = "assets.json") -> list[dict]:
    try:
        with open(items_path) as f:
            return json.load(f)
    except FileNotFoundError:
        demo = [
            {"id": 1, "name": "Laptop", "custodian": "Alice", "due_date": "2025-12-31", "condition": "Good"},
            {"id": 2, "name": "Monitor", "custodian": "Bob", "due_date": "2025-11-15", "condition": "Fair"}
        ]
        Path(items_path).write_text(json.dumps(demo, indent=2))
        return demo
