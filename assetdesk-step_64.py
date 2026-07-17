# === Stage 64: Add validation for relationship references ===
# Project: AssetDesk
class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def validate_reference(ref_value, ref_type, available_ids=None):
    """Validate that a reference value is non-empty and exists if an ID set is provided."""
    if not isinstance(ref_value, str) or not ref_value.strip():
        raise ValidationError(f"{ref_type} must be a non-empty string")
    ref_id = ref_value.strip()
    if available_ids is not None:
        if ref_id not in available_ids:
            raise ValidationError(
                f"{ref_type} '{ref_id}' not found. Available IDs: {available_ids}"
            )


def validate_due_date(due_str):
    """Validate that a due date string matches YYYY-MM-DD format and is not past."""
    if not isinstance(due_str, str) or len(due_str) != 10:
        raise ValidationError(f"Due date must be in YYYY-MM-DD format")
    try:
        parts = due_str.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValidationError(f"Due date values out of range: {due_str}")
    except ValueError as e:
        raise ValidationError(f"Invalid due date format: {e}") from e
