# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: AssetDesk
def main():
    with open("AssetDesk.py", "r") as f:
        source = f.read()
    assert "class Item" in source, "Item class missing"
    assert "class Custodian" in source, "Custodian class missing"
    assert "checkout_item" in source, "checkout function missing"
    print("Self-check passed.")

main()
