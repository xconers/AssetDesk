# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: AssetDesk
def repair_data_integrity(items, custodians):
    """Fix simple data integrity issues in AssetDesk records."""
    # Ensure all items have required fields with defaults
    for item in items:
        if 'condition' not in item or not isinstance(item['condition'], str):
            item.setdefault('condition', 'Unknown')
        if 'notes' not in item:
            item['notes'] = ''
        if 'due_date' not in item:
            item['due_date'] = None
        # Auto-assign custodian if missing
        if 'custodian_id' not in item or item['custodian_id'] is None:
            if custodians:
                item['custodian_id'] = custodians[0]['id']

    # Ensure all custodians have required fields
    for c in custodians:
        if 'name' not in c or not isinstance(c['name'], str):
            c.setdefault('name', 'Unknown Custodian')
        if 'email' not in c:
            c['email'] = ''

    return items, custodians
