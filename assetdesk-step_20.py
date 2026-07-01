# === Stage 20: Add duplicate detection for newly created records ===
# Project: AssetDesk
from typing import Optional, Tuple
import hashlib
def _get_record_hash(record: dict) -> str:
    return hashlib.sha256(str(sorted(record.items())).encode()).hexdigest()[:10]
class DuplicateDetector:
    def __init__(self, existing_records: list[dict], tolerance_seconds: int = 3600):
        self.existing_hashes = {_get_record_hash(r): r for r in existing_records}
        self.tolerance = tolerance_seconds
    def check(self, new_record: dict) -> Tuple[bool, Optional[dict]]:
        if not isinstance(new_record, dict): return False, None
        base_record = {k: v for k, v in new_record.items() if k != 'created_at'}
        hash_key = _get_record_hash(base_record)
        if hash_key in self.existing_hashes:
            existing = self.existing_hashes[hash_key]
            return True, existing
        return False, None
