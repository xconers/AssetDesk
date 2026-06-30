# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: AssetDesk
from typing import Optional, Callable
import sys

def dry_run_wrapper(func: Callable[..., bool], *args: tuple, **kwargs: dict) -> bool:
    if args.get('_dry_run', False):
        print(f"[DRY-RUN] Would execute {func.__name__} with args={args}, kwargs={kwargs}")
        return True
    try:
        result = func(*args, **kwargs)
        return result
    except Exception as e:
        if not args.get('_dry_run', False):
            raise
