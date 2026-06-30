# === Stage 16: Add argparse support for the most common commands ===
# Project: AssetDesk
import argparse

def main():
    parser = argparse.ArgumentParser(description="AssetDesk CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # checkout command
    p_checkout = subparsers.add_parser('checkout', help='Check out an item')
    p_checkout.add_argument('--item-id', required=True, help='Item ID')
    p_checkout.add_argument('--custodian', required=True, help='Custodian name')
    p_checkout.add_argument('--due-date', required=True, help='Due date (YYYY-MM-DD)')

    # checkin command
    p_checkin = subparsers.add_parser('checkin', help='Check in an item')
    p_checkin.add_argument('--item-id', required=True, help='Item ID')
    p_checkin.add_argument('--condition', default='Good', help='Condition note (default: Good)')

    # list command
    p_list = subparsers.add_parser('list', help='List all items')
    p_list.add_argument('--status', choices=['all', 'active', 'returned'], default='all', help='Filter by status')

    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Placeholder for actual logic implementation based on command
    print(f"Executing command: {args.command}")
    if hasattr(args, 'item_id'):
        print(f"Item ID: {args.item_id}")
    if hasattr(args, 'custodian'):
        print(f"Custodian: {args.custodian}")
    if hasattr(args, 'due_date'):
        print(f"Due Date: {args.due_date}")
    if hasattr(args, 'condition'):
        print(f"Condition: {args.condition}")
    if hasattr(args, 'status'):
        print(f"Status Filter: {args.status}")

    return 0

if __name__ == "__main__":
    exit(main())
