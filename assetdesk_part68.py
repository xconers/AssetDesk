# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: AssetDesk
# assetdesk/changelog.py – compact changelog derived from activity log

from collections import defaultdict, deque


def build_changelog(activity_log: list[dict], max_entries: int = 50) -> str:
    """Return a short bullet-list summary of the most recent activities."""
    if not activity_log:
        return "No activity recorded yet."

    entries = deque(activity_log[-max_entries:])
    grouped = defaultdict(list)
    for act in entries:
        ts, kind, target, detail = (act.get(k, "") for k in ("timestamp", "kind", "target", "detail"))
        key = f"{ts} | {kind}" if ts else kind
        grouped[key].append(f"  • {detail}")

    lines = ["AssetDesk Changelog:\n"] + [f"- {key}\n" + "".join(v) for v in grouped.values()]
    return "\n".join(lines)


if __name__ == "__main__":
    print(build_changelog([
        {"timestamp": "2025-06-12", "kind": "checkout", "target": "Laptop-A", "detail": "issued to Alice"},
        {"timestamp": "2025-06-13", "kind": "return",    "target": "Laptop-A", "detail": "returned in good condition"},
    ]))
