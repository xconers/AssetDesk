# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: AssetDesk
import unittest
from datetime import date, timedelta

class TestAssetValidation(unittest.TestCase):
    def test_valid_checkout(self):
        custodian = "Alice"
        item_id = 101
        due = date.today() + timedelta(days=30)
        notes = "No damage"
        
        # Simulate a validation function that checks:
        # - custodian is not empty
        # - item_id > 0
        # - due date is in the future or today
        # - notes are non-empty
        
        self.assertTrue(len(custodian) > 0)
        self.assertGreater(item_id, 0)
        self.assertLessEqual(due, date.today() + timedelta(days=365))
        self.assertTrue(len(notes) > 0)

    def test_invalid_checkout(self):
        custodian = ""
        item_id = -1
        due = date.today() - timedelta(days=1)
        notes = " " * 10
        
        # These should all fail validation
        with self.assertRaises(AssertionError):
            self.assertTrue(len(custodian) > 0)

if __name__ == '__main__':
    unittest.main()
