# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: AssetDesk
class AssetDeskManager:
    def delete_item(self, item_id: int, confirm: bool = False) -> bool:
        if not self._items.get(item_id):
            return False
        if not confirm and input(f"Удалить актив #{item_id}? (y/n): ").lower() != 'y':
            print("Операция отменена.")
            return False
        del self._items[item_id]
        print(f"Актив #{item_id} успешно удален.")
        return True

    def delete_custodian(self, custodian_name: str) -> bool:
        if not any(c.name == custodian_name for c in self.custodians):
            return False
        confirm = input(f"Удалить хранителя {custodian_name}? (y/n): ").lower() == 'y'
        if confirm:
            self.custodians = [c for c in self.custodians if c.name != custodian_name]
            print(f"Хранитель {custodian_name} удален.")
            return True
        print("Операция отменена.")
        return False

    def delete_audit_report(self, report_id: int) -> bool:
        if not self._reports.get(report_id):
            return False
        confirm = input(f"Удалить отчет #{report_id}? (y/n): ").lower() == 'y'
        if confirm:
            del self._reports[report_id]
            print(f"Отчет #{report_id} удален.")
            return True
        print("Операция отменена.")
        return False
