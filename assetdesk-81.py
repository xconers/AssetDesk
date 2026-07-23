# === Stage 81: Add final README text as a module string with usage examples ===
# Project: AssetDesk
def asset_desk_usage_example():
    """Demonstrate AssetDesk core workflow in a compact, self-contained example."""
    from datetime import date, timedelta

    # 1. Register custodians and items
    custodian_alice = Custodian("Alice", "alice@edu.org")
    item_laptop = Item("Laptop-2024", "SN-LAP-98765", "Good", custodian_alice)

    # 2. Create a checkout record with due date, condition note, and audit trail
    today = date.today()
    checkout = CheckoutRecord(
        item=item_laptop,
        borrower=custodian_alice,
        due_date=today + timedelta(days=14),
        condition_note="Screen works fine; battery at 82%.",
        status="Active",
    )

    # 3. Retrieve and display the audit report for this item
    report = checkout.generate_audit_report()
    print("=" * 60)
    print(report)
    print("=" * 60)

    # 4. Return the item early — update status, log return event
    returned_date = today - timedelta(days=1)  # simulate past due date for demo
    checkout.return_item(returned_date)
    print(f"Item '{checkout.item.name}' returned on {returned_date}.")

if __name__ == "__main__":
    asset_desk_usage_example()
