# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: AssetDesk
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Asset:
    id: str
    name: str
    category: str
    custodian_id: Optional[str] = None
    due_date: Optional[date] = None
    condition_note: Optional[str] = None
    audit_report_path: Optional[str] = None

@dataclass
class AuditReport:
    asset_id: str
    date_checked: date
    status: str  # "passed", "failed"
    notes: str = ""
