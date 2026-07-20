# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: AssetDesk
from datetime import date, timedelta


def snapshot_diff(before: dict | None, after: dict) -> list[dict]:
    """Compare a before-state to an after-state and return the changed keys."""
    if not isinstance(before, dict):
        before = {}
    changes = []
    for key in set(list(before.keys()) + list(after.keys())):
        old_val = before.get(key)
        new_val = after.get(key)
        if old_val != new_val:
            changes.append({"key": key, "before": old_val, "after": new_val})
    return changes


def report_snapshot(before: dict | None, after: dict, title: str = "Snapshot") -> str:
    """Produce a human-readable before/after comparison."""
    diff = snapshot_diff(before, after)
    lines = [f"=== {title} ===", f"{len(diff)} change(s):"]
    for ch in diff:
        lines.append(f"  [{ch['key']}] {ch['before']} → {ch['after']}")
    return "\n".join(lines)


if __name__ == "__main__":
    before = {"item_id": "A1", "status": "checked_out", "due_date": date(2025, 4, 1), "note": ""}
    after = {"item_id": "A1", "status": "returned", "due_date": date(2025, 3, 1), "note": "damaged"}
    print(report_snapshot(before, after))
