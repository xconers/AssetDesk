# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: AssetDesk
def manage_tags(item, tags_to_add=None, tags_to_remove=None):
    if item.get('tags') is None:
        item['tags'] = set()
    for tag in (tags_to_add or []):
        item['tags'].add(tag)
    for tag in (tags_to_remove or []):
        item['tags'].discard(tag)

def generate_tag_summary(items, min_count=1):
    from collections import Counter
    all_tags = [tag for item in items if isinstance(item.get('tags'), set) for tag in item['tags']]
    return {tag: count for tag, count in Counter(all_tags).items() if count >= min_count}
