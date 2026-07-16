# === Stage 61: Add performance timing for core list and search operations ===
# Project: AssetDesk
import time
from functools import wraps


def profile(func):
    """Wrap a function to measure and print its execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"  {func.__name__}: {elapsed_ms:.2f} ms")
        return result
    return wrapper


@profile
def _list_items(self):
    """Return all items in the AssetDesk instance."""
    return list(self.items.values())


@profile
def _search_items(self, query):
    """Search items by keyword matching title or custodian name."""
    results = []
    for item_id, item in self.items.items():
        if (query.lower() in item.title.lower() or
                query.lower() in item.custodian_name.lower()):
            results.append(item)
    return results


def register_timed_operations(self):
    """Register performance-timed list and search operations."""
    self.list_items = _list_items
    self.search_items = _search_items
