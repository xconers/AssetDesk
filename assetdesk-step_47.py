# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: AssetDesk
def demo():
    """Walk through a typical AssetDesk workflow."""
    from assetdesk import Item, Custodian, Checkout, AuditReport
    from datetime import date, timedelta

    cust = Custodian("Alice", email="alice@example.com")
    item  = Item("Laptop-042", category="Electronics", condition="Good")
    checkout = Checkout(item, cust, due_date=date.today() + timedelta(days=14), note="For data analysis")

    print(f"Checked out: {checkout.item.serial} to {cust.name}, due {checkout.due_date}")

    report = AuditReport([checkout])
    print(report)

demo()
