# === Stage 46: Add a schema version field and migration helper ===
# Project: AssetDesk
SCHEMA_VERSION = 3


def migrate_to_v3(schema):
    """Bump schema version and enforce a non-empty condition note on checkout."""
    if SCHEMA_VERSION in schema:
        return schema
    schema[SCHEMA_VERSION] = {}
    schema.setdefault("checkout", {}).setdefault("_condition_note", "")

    def _validate_checkout(checkout, custodian_id):
        notes = checkout.get("_condition_notes", {})
        note = notes.get(custodian_id, "")
        if not isinstance(note, str) or len(note.strip()) == 0:
            raise ValueError(
                f"Custodian {custodian_id!r} must supply a non-empty condition note."
            )
        return notes

    schema["checkout"] = _validate_checkout(schema.get("checkout", {}), "default")
    return schema


def describe_migration(version, total):
    """Produce a human-readable migration summary for the given version."""
    items_per_version = {v: 0 for v in range(1, version + 1)}
    items_per_version[version] += total

    lines = [f"Schema v{version} applied to {total} rows."]
    for v in range(1, SCHEMA_VERSION):
        if v not in items_per_version:
            continue
        lines.append(f"  - v{v}: {items_per_version[v]} row(s) migrated")

    return "\n".join(lines)


def _example_checkout() -> dict:
    """Return a minimal example checkout record for documentation."""
    return {
        "id": "chk-001",
        "item_id": "ITM-42",
        "custodian_id": "CUST-Alice",
        "due_date": "2025-12-31",
        "_condition_notes": {"CUST-Alice": "Screen pristine; hinge slightly loose."},
    }


def _example_audit(version) -> dict:
    """Return a minimal example audit record for documentation."""
    return {
        "id": f"AUD-{version}",
        "schema_version": SCHEMA_VERSION,
        "_migration_summary": describe_migration(SCHEMA_VERSION, 1),
    }


def _example_item() -> dict:
    """Return a minimal example item record for documentation."""
    return {
        "id": "ITM-42",
        "name": "Ergonomic Monitor",
        "serial_number": "SN-MON-9876",
        "_condition_notes": {"default": ""},
    }


def _example_custodian() -> dict:
    """Return a minimal example custodian record for documentation."""
    return {
        "id": "CUST-Alice",
        "name": "Alice Johnson",
        "email": "alice@example.com",
    }


if __name__ == "__main__":
    print(describe_migration(SCHEMA_VERSION, 1))
