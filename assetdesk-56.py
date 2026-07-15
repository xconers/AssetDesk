# === Stage 56: Add compact error classes for domain failures ===
# Project: AssetDesk
class AssetDeskError(Exception):
    """Base for all domain-specific failures in AssetDesk."""


class ItemNotFoundError(AssetDeskError, KeyError):
    pass


class CustodianNotFoundError(AssetDeskError, KeyError):
    pass


class CheckoutConflictError(AssetDeskError):
    """Raised when an item is already checked out to someone else or overdue."""


class ConditionMismatchError(AssetDeskError, ValueError):
    """Raised when a condition note contradicts the expected state."""


class AuditReportFailure(AssetDeskError):
    """Raised when generating or parsing an audit report fails."""


class PermissionDenied(AssetDeskError, RuntimeError):
    pass


class InvalidDate(AssetDeskError, ValueError):
    def __init__(self, date_str: str) -> None:
        super().__init__(f"Invalid date string: {date_str!r}")
