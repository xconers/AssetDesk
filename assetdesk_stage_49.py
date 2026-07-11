# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: AssetDesk
import unittest
from assetdesk.models import Item, Custodian


class TestUpdateDeleteEdgeCases(unittest.TestCase):
    def setUp(self):
        self.item = Item(
            item_id="ITEM001",
            name="Laptop",
            custodian=Custodian(custodian_id="CUST01", name="Alice"),
            due_date="2025-12-31"
        )

    def test_update_overrides_all_fields(self):
        self.item.name = "Old Laptop"
        item_repo = ItemRepository()
        updated = item_repo.update(self.item)
        self.assertEqual(updated.name, "Old Laptop")
        self.assertNotEqual(updated.custodian.custodian_id, "")

    def test_update_preserves_due_date_when_not_set(self):
        self.item.due_date = None
        item_repo = ItemRepository()
        updated = item_repo.update(self.item)
        self.assertIsNone(updated.due_date)

    def test_delete_returns_none_for_missing_item(self):
        deleted = ItemRepository().delete("NONEXISTENT")
        self.assertIsNone(deleted)

    def test_update_with_invalid_due_date_ignored(self):
        self.item.due_date = "not-a-date"
        item_repo = ItemRepository()
        updated = item_repo.update(self.item)
        self.assertNotEqual(updated.due_date, "not-a-date")


if __name__ == "__main__":
    unittest.main()
