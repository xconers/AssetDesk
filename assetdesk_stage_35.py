# === Stage 35: Add active user switching and user-specific records ===
# Project: AssetDesk
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def check_out(self, item, custodian, due_date):
        record = CheckoutRecord(item=item, custodian=custodian, due_date=due_date)
        return record

    def return_item(self, record):
        if record.due_date and datetime.now() > record.due_date:
            print(f"Warning: {record.item.name} was overdue for {self.name}")
        else:
            print(f"{self.name} returned {record.item.name} on time.")

    def audit_report(self, records):
        return f"Audit by {self.name}: {len(records)} items checked."
