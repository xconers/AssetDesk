# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: AssetDesk
import signal
from rich.console import Console

console = Console()


def _handle_signal(signum, frame):
    """Gracefully exit on Ctrl+C."""
    console.print("\n[bold red]AssetDesk interrupted by user.[/]")
    sys.exit(1)


signal.signal(signal.SIGINT, _handle_signal)
