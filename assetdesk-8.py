# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: AssetDesk
class FilterManager:
    def __init__(self, items):
        self.items = items
    
    def filter_by_status(self, status):
        return [item for item in self.items if item.get('status') == status]
    
    def filter_by_category(self, category):
        return [item for item in self.items if item.get('category') == category]
    
    def filter_by_owner(self, owner):
        return [item for item in self.items if item.get('owner') == owner]
    
    def filter_by_tag(self, tag):
        return [item for item in self.items if any(tag.lower() in t.lower() for t in item.get('tags', []))]
    
    def apply_multiple_filters(self, **kwargs):
        filtered = self.items
        for key, value in kwargs.items():
            if value is None:
                continue
            if callable(getattr(self, f'filter_by_{key}')):
                filtered = getattr(self, f'filter_by_{key}')(value)
            else:
                raise ValueError(f"Unknown filter type: {key}")
        return filtered
