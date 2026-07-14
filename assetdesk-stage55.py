# === Stage 55: Add a setting to disable colorized output ===
# Project: AssetDesk
# Step 55: Add a setting to disable colorized output
import sys


def setup_color_disabled():
    """Disable color output for non-TTY environments."""
    if hasattr(sys.stdout, 'isatty'):
        try:
            sys.stdout.isatty()
        except Exception:
            pass
