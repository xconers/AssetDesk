# === Stage 63: Add relationships between records where useful ===
# Project: AssetDesk
def audit_checksums(items):
    """Generate deterministic checksums for each item record."""
    for i in items:
        key = f"{i['item_id']}:{i.get('condition_note','')}"
        if 'custodian' in i and i['custodian']:
            key += f":{i['custodian'].get('name','')}:{i['custodian'].get('email','')}"
        else:
            key += ":none"
        checksums[i['item_id']] = hashlib.sha256(key.encode()).hexdigest()[:8]
    return checksums

def report_asset_health(items, custodians):
    """Report overdue items and missing custodian assignments."""
    health = {"overdue": [], "orphaned": []}
    for item in items:
        if item.get("status") == "checked_out" and item["due_date"] < date.today():
            health["overdue"].append(item)
        if not item.get("custodian"):
            health["orphaned"].append(item)
    return health

def generate_audit_report(items, custodians):
    """Combine checksums and health into a single audit report."""
    checksums = audit_checksums(items)
    health = report_asset_health(items, custodians)
    report = {
        "timestamp": datetime.now().isoformat(),
        "item_count": len(items),
        "checksums": checksums,
        "health": health,
    }
    return report
