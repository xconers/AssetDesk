# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: AssetDesk
def score_item(item: dict) -> tuple[int, str]:
    """Return a priority score and label for an asset."""
    overdue = (item.get("due_date", "9999-12-31") < item.get("checkout_date", ""))
    no_return = not bool(item.get("return_status"))
    notes = item.get("notes", "").lower()
    risk_words = {"damaged": 0.6, "broken": 0.7, "critical": 0.8}
    penalty = sum(risk_words.get(w, 0) for w in notes.split())
    score = (1 if overdue else 0) + (1 if no_return else 0) + penalty
    label = {0: "OK", 1: "Watch", 2: "Action", 3: "Urgent"}.get(score, f"Score:{score}")
    return score, label
