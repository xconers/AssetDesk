# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: AssetDesk
class AssetDesk:
    def __init__(self):
        self.items = {}
        self.dates = {}
        self.conditions = {}
        self.custodians = {}
        self.confirmed_clear = False

    def add_item(self, name):
        if name in self.items: return "Already exists"
        self.items[name] = []
        return f"Added {name}"

    def add_custodian(self, custodian, item):
        if item not in self.items: return "Item does not exist"
        self.custodians[item] = custodian
        return f"Custodian set to {custodian} for {item}"

    def clear_all(self):
        if not self.confirmed_clear: return "Not confirmed. Use confirm_clear() first."
        self.items.clear()
        self.dates.clear()
        self.conditions.clear()
        self.custodians.clear()
        self.confirmed_clear = False
        return "All data cleared"

    def confirm_clear(self):
        if not self.items and not self.dates and not self.conditions and not self.custodians:
            return "Nothing to clear"
        self.confirmed_clear = True
        return "Clear confirmed. Run clear_all() to reset."
