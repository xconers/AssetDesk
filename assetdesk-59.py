# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: AssetDesk
def bulk_delete(items, confirm=False):
    """Delete multiple items at once if confirmed by the user."""
    if not confirm:
        print("Bulk delete requires explicit confirmation.")
        return False
    deleted = [item for item in items]
    del items[:]
    print(f"Deleted {len(deleted)} items.")
    return True
