# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: AssetDesk
def demo():
    from assetdesk import CheckoutDesk, AssetItem, Custodian, AuditReport
    desk = CheckoutDesk()
    cust1 = Custodian("Alice", "alice@example.com")
    cust2 = Custodian("Bob", "bob@example.com")
    item1 = AssetItem("Laptop Pro 15", "ALP-001", "Good", cust1)
    item2 = AssetItem("Mouse Wireless", "MW-042", "Fair", cust2)
    desk.checkout(item1, cust2, due="2026-03-15")
    desk.checkout(item2, cust1, due="2026-02-28")
    print("=== AssetDesk End-to-End Demo ===")
    for rec in desk.records:
        print(f"  {rec.item.name} -> {rec.custodian.name}, due {rec.due_date}")
    audit = AuditReport(desk)
    print(audit.summary())
