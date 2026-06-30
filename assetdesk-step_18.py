# === Stage 18: Add an activity log with timestamps and action names ===
# Project: AssetDesk
class ActivityLog:
    def __init__(self, log_file="logs/activity.log"):
        self.file = open(log_file, "a", encoding="utf-8")

    def record(self, action_name, user=None):
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] ACTION: {action_name}"
        if user:
            entry += f" | USER: {user}"
        self.file.write(entry + "\n")
        self.file.flush()

    def close(self):
        self.file.close()
