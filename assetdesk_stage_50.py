# === Stage 50: Add unit tests for import and export behavior ===
# Project: AssetDesk
import unittest
from datetime import date, timedelta

class TestCheckoutImportExport(unittest.TestCase):

    def test_deserialize_roundtrip(self):
        raw = {
            "id": 1, "name": "Laptop", "owner_id": 5, "custodian_id": 3,
            "due_date": (date.today() + timedelta(days=7)).isoformat(),
            "status": "CheckedOut", "condition_notes": "Screen cracked"
        }
        asset = AssetCheckout.deserialize(raw)
        self.assertEqual(asset.id, 1)
        self.assertEqual(asset.name, "Laptop")
        self.assertEqual(asset.status, "CheckedOut")
        self.assertEqual(asset.condition_notes, "Screen cracked")

    def test_serialize_roundtrip(self):
        asset = AssetCheckout(id=2, name="Monitor", owner_id=5, custodian_id=3,
                               due_date=date.today() + timedelta(days=14),
                               status="CheckedIn", condition_notes="Good")
        data = asset.serialize()
        restored = AssetCheckout.deserialize(data)
        self.assertEqual(asset.id, restored.id)
        self.assertEqual(asset.name, restored.name)

    def test_deserialize_invalid_json_raises(self):
        with self.assertRaises(ValueError):
            AssetCheckout.deserialize("{not valid json}")

if __name__ == "__main__":
    unittest.main()
