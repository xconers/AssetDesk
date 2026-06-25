# === Stage 4: Implement create operations for the primary records ===
# Project: AssetDesk
from datetime import date, timedelta
import uuid

def create_item(name: str, custodian_id: int, due_date: date, condition_note: str = "") -> dict:
    item_uuid = str(uuid.uuid4())
    return {
        "id": item_uuid,
        "name": name,
        "custodian_id": custodian_id,
        "due_date": due_date.isoformat(),
        "condition_note": condition_note,
        "status": "active"
    }

def create_custodian(name: str, department: str) -> dict:
    custodian_uuid = str(uuid.uuid4())
    return {
        "id": custodian_uuid,
        "name": name,
        "department": department,
        "created_at": date.today().isoformat()
    }

def create_audit_report(item_id: str, auditor_name: str) -> dict:
    report_uuid = str(uuid.uuid4())
    return {
        "id": report_uuid,
        "item_id": item_id,
        "auditor_name": auditor_name,
        "timestamp": date.today().isoformat(),
        "status": "pending"
    }
