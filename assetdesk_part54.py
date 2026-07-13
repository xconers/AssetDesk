# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: AssetDesk
def colorize(text, style):
    """Return ANSI-colored text; safe if stdout is not a terminal."""
    try:
        import sys
        if not hasattr(sys.stdout, 'isatty') or sys.stdout.isatty():
            return f"\033[{style}m{text}\033[0m"
    except Exception:
        pass
    return text

COLORS = {
    "red":     31, "green":   32, "yellow": 33,
    "blue":    34, "purple":  35, "cyan":   36,
    "white":   37, "bold":   None, "muted": 90,
}

def styled(text, kind="normal"):
    if kind == "error":       return colorize(f"[{text}]     ", COLORS["red"])
    if kind == "success":     return colorize(f"[{text}]     ", COLORS["green"])
    if kind == "warning":     return colorize(f"[{text}]     ", COLORS["yellow"])
    if kind == "info":        return colorize(f"[{text}]     ", COLORS["blue"])
    if kind == "header":      return colorize(f"== {text} ==", COLORS["cyan"] + 1)
    return f"[{text}]     "
