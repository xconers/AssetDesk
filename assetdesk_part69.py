# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: AssetDesk
def reset_demo_data(db):
    with db.cursor() as c:
        c.execute("DELETE FROM audit_logs")
        c.execute("DELETE FROM condition_notes")
        c.execute("DELETE FROM custodians")
        c.execute("DELETE FROM items")
        c.execute("DELETE FROM checkout_requests")
        print("[AssetDesk] Demo data reset complete.")
