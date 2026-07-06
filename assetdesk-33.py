# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: AssetDesk
DEFAULT_SETTINGS = {
    "checkout_timeout_hours": 72,
    "auto_renew_days_before_expiry": 3,
    "condition_note_max_length": 500,
    "audit_report_csv_delimiter": ",",
    "date_format": "%Y-%m-%d",
}

def get_setting(name):
    return DEFAULT_SETTINGS.get(name)

def set_setting(name, value):
    if name not in DEFAULT_SETTINGS:
        raise ValueError(f"Unknown setting: {name}")
    DEFAULT_SETTINGS[name] = value
