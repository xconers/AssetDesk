# === Stage 58: Add bulk update behavior for selected records ===
# Project: AssetDesk
def bulk_update_records(records, updates):
    """Bulk update records with a dict of field->value mappings."""
    updated = []
    for record in records:
        for key, value in updates.items():
            if hasattr(record, key) and not callable(getattr(record, key)):
                setattr(record, key, value)
        updated.append(record)
    return updated

def bulk_set_due_date(records, new_date):
    """Set the due date on all records."""
    for record in records:
        if hasattr(record, 'due_date'):
            record.due_date = new_date
    return records

def bulk_add_condition_notes(records, note):
    """Append a condition note to each record's notes list."""
    for record in records:
        if hasattr(record, 'notes') and isinstance(record.notes, list):
            record.notes.append(note)
    return records
