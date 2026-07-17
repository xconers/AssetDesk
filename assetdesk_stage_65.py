# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: AssetDesk
def merge_imports(existing, new):
    """Merge two sets of import strings, removing exact duplicates."""
    return list(dict.fromkeys(new + existing))
