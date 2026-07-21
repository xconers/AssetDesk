# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: AssetDesk
from datetime import date, timedelta

# ── helpers for checkout reporting ────────────────────────────────────────

def _format_due(due: date) -> str:
    """Return a human-readable label describing how close the due date is."""
    if d < date.today():
        return "OVERDUE"
    remaining = (d - date.today()).days
    if 0 <= remaining <= 7:
        return f"{remaining} days left"
    return str(remaining) + " days away"

def _format_condition(note: str | None) -> str:
    """Collapse a condition note to a short status token."""
    if not note:
        return "?"
    key = note[:4].upper()
    mapping = {
        "GOOD": "OK",
        "FINE": "OK",
        "SCRATCHED": "DAMAGED",
        "CRACKED": "DAMAGED",
        "BROKEN": "UNFIT",
        "LOST": "MISSING",
        "UNKNOWN": "?",
    }
    return mapping.get(key, note[:10])

def _format_custodian(cust: dict) -> str:
    """Render a custodian record as 'name (id)'."""
    return f"{cust['name']} ({cust['id']})"

def render_checkout_report(items: list[dict], due_cutoff_days: int = 30) -> str:
    """Build a compact audit report from a list of checkout items.

    Parameters
    ----------
    items : list[dict]
        Each dict must contain at least: id, custodian, due_date, condition.
    due_cutoff_days : int
        Items whose remaining days are <= this threshold are flagged as urgent.

    Returns
    -------
    str
        A multi-line report grouped by urgency status.
    """
    today = date.today()
    groups: dict[str, list[dict]] = {"OK": [], "URGENT": [], "OVERDUE": []}
    for it in items:
        due = date.fromisoformat(it["due_date"])
        remaining = (due - today).days
        if remaining < 0:
            status = "OVERDUE"
        elif remaining <= due_cutoff_days:
            status = "URGENT"
        else:
            status = "OK"
        groups[status].append(
            {**it, "_label": f"{_format_custodian(it['custodian'])} — {_format_due(due)} [{_format_condition(it.get('condition'))}]"}
        )

    lines = ["=== AssetDesk Checkout Report ==="]
    for status in ("OK", "URGENT", "OVERDUE"):
        entries = groups[status]
        if not entries:
            continue
        header = f"[{status}] ({len(entries)} item{'s' if len(entries) > 1 else ''})"
        lines.append(header)
        for ent in entries:
            lines.append(f"  • {ent['_label']}")
    lines.append("")
    return "\n".join(lines)
