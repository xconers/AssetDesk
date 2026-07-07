# === Stage 34: Add support for multiple local user profiles ===
# Project: AssetDesk
import os, json

def load_user_profiles(path=None):
    """Load all user profile JSON files from a directory."""
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "profiles")
    profiles = {}
    for fname in sorted(os.listdir(path)):
        if fname.endswith(".json"):
            with open(os.path.join(path, fname)) as f:
                profiles[fname[:-5]] = json.load(f)
    return profiles

def save_user_profile(path=None, name="user", data=None):
    """Save a single user profile to JSON."""
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "profiles")
    os.makedirs(path, exist_ok=True)
    fname = f"{name}.json"
    with open(os.path.join(path, fname), "w") as f:
        json.dump(data, f, indent=2)
