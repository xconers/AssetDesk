# === Stage 19: Add undo support for the last simple mutation ===
# Project: AssetDesk
import json
from datetime import datetime, timedelta

class AssetDeskUndo:
    def __init__(self):
        self.history = []
        self.max_history = 10
    
    def record(self, action_type, data):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_type,
            "data": data
        }
        self.history.append(entry)
        if len(self.history) > self.max_history:
            del self.history[0]

    def undo_last(self):
        if not self.history:
            return None
        last = self.history.pop()
        return {
            "action": last["action"],
            "data": last["data"]
        }
