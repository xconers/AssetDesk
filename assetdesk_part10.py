# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: AssetDesk
def search_assets(query, fields=None):
    if fields is None:
        fields = ['name', 'custodian', 'location']
    query_lower = query.lower()
    results = [item for item in assets if any(query_lower in str(getattr(item, field, '')).lower() for field in fields)]
    return results
