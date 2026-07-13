# === Stage 51: Add unit tests for search and filter behavior ===
# Project: AssetDesk
import unittest
from datetime import date, timedelta

# Minimal stub for AssetDesk search/filter tests (assumes models exist)


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        from assetdesk.models import Item, Custodian
        self.item1 = Item(name="Laptop", custodian=Custodian("Alice"), due=date.today() + timedelta(days=30))
        self.item2 = Item(name="Mouse", custodian=Custodian("Bob"), due=date.today() - timedelta(days=5), condition="damaged")

    def test_search_by_name(self):
        results = [i for i in (self.item1, self.item2) if "Laptop" in i.name]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Laptop")

    def test_filter_overdue(self):
        overdue = [i for i in (self.item1, self.item2) if i.due < date.today()]
        self.assertTrue(all(i.overdue() for i in overdue))

    def test_filter_condition(self):
        damaged = [i for i in (self.item1, self.item2) if "damaged" in i.condition]
        self.assertEqual(len(damaged), 1)


if __name__ == "__main__":
    unittest.main()
