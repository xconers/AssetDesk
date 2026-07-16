# === Stage 60: Add saved views for frequently used filters ===
# Project: AssetDesk
class SavedView:
    def __init__(self, name, filters=None, sort_by="due_date", order="asc"):
        self.name = name
        self.filters = filters or {}
        self.sort_by = sort_by
        self.order = order

    def apply(self, records):
        result = list(records)
        for key, value in self.filters.items():
            if isinstance(value, tuple):
                result = [r for r in result if getattr(r, key) in value[0]]
            else:
                result = [r for r in result if getattr(r, key) == value]
        reverse = self.order == "desc"
        return sorted(result, key=lambda x: (x.sort_by or x.due_date), reverse=reverse)

    def __repr__(self):
        return f"<SavedView {self.name} filters={self.filters}>"


def register_saved_view(name, **kwargs):
    return SavedView(name=name, filters=kwargs.get("filters", {}), sort_by=kwargs.get("sort_by", "due_date"), order=kwargs.get("order", "asc"))


# Example usage:
my_view = register_saved_view("Overdue Items", filters={"status": "checked_out"}, sort_by="due_date", order="asc")
