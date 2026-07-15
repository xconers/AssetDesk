# === Stage 57: Add structured result objects for command handlers ===
# Project: AssetDesk
class CheckoutResult:
    """Structured result for an asset checkout handler."""
    def __init__(self, item_id: int = None, custodian_name: str = "", due_date: str = "", notes: str = ""):
        self.item_id = item_id
        self.custodian_name = custodian_name
        self.due_date = due_date
        self.notes = notes

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}


class AuditResult:
    """Structured result for an audit report handler."""
    def __init__(self, report_title: str = "", total_items: int = 0, missing_count: int = 0, issues: list = []):
        self.report_title = report_title
        self.total_items = total_items
        self.missing_count = missing_count
        self.issues = issues

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}


class ErrorResult:
    """Structured error response from any handler."""
    def __init__(self, message: str = "", code: int = 400, details: dict = {}):
        self.message = message
        self.code = code
        self.details = details

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
