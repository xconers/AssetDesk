# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: AssetDesk
from dataclasses import dataclass, field
from datetime import date, timedelta
import random

@dataclass
class Asset:
    id: str
    name: str
    custodian: str | None = None
    due_date: date | None = None
    condition_notes: str = ""

def init_demo_data():
    items = [Asset(f"IT-{i}", f"Laptop {i}") for i in range(1, 6)]
    random.shuffle(items)
    today = date.today()
    for item in items[:3]:
        item.due_date = today + timedelta(days=random.randint(7, 30))
        item.custodian = f"User_{random.randint(1,5)}"
    return {item.id: item}
