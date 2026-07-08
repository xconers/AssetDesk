# === Stage 38: Add data integrity checks for broken references ===
# Project: AssetDesk
def check_references(items: dict, custodians: list) -> set[str]:
    """Validate that every item references a valid custodian and return broken IDs."""
    broken = set()
    for i in items.values():
        if i.get("custodian_id") not in {c["id"] for c in custodians}:
            broken.add(i["id"])
    return broken
