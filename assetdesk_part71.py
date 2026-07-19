# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: AssetDesk
def seed_demo_data(db):
    """Insert a fixed set of demo rows so AssetDesk can be explored immediately."""
    db.execute("DELETE FROM audit_log")
    db.execute("DELETE FROM custodian WHERE id > 0")
    db.execute("DELETE FROM item WHERE id > 0")

    # Custodians
    db.executemany(
        "INSERT INTO custodian (first_name, last_name, email) VALUES (?, ?, ?)",
        [
            ("Alice", "Johnson", "alice@example.com"),
            ("Bob", "Smith", "bob@example.com"),
            ("Carol", "Williams", "carol@example.com"),
        ],
    )

    # Items with different statuses and conditions
    db.executemany(
        """INSERT INTO item (name, custodian_id, checkout_date, due_date, condition_notes)
         VALUES (?, ?, ?, ?, ?)""",
        [
            ("Laptop", 1, "2025-03-01", "2025-04-01", "No scratches"),
            ("Headphones", 1, "2025-03-05", "2025-04-05", "Slight wear"),
            ("Monitor", 2, "2025-03-10", "2025-04-10", "Screen OK"),
            ("Keyboard", 2, "2025-03-15", "2025-04-15", "Backlight dim"),
            ("Mouse", 3, "2025-03-20", "2025-04-20", "Click works"),
        ],
    )

    # Audit log showing past checkouts and returns
    db.executemany(
        """INSERT INTO audit_log (user_id, action, target_type, target_id, timestamp)
         VALUES (?, ?, ?, ?, ?)""",
        [
            (1, "check_in", "item", 1, "2025-03-01T09:00:00"),
            (1, "check_out", "item", 1, "2025-03-08T14:00:00"),
            (1, "check_in", "item", 1, "2025-04-01T10:00:00"),
            (1, "check_out", "item", 2, "2025-03-05T08:30:00"),
        ],
    )
