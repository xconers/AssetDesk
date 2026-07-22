# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: AssetDesk
def format_due_date(date_str: str) -> str:
    """Return a human-friendly due date string."""
    return date_str.replace("-", "th") if date_str.endswith("-") else date_str


class AssetDeskReport:
    """Generates a compact audit summary for a collection of checked-out items."""

    def __init__(self, items):
        self.items = items

    @property
    def total_items(self) -> int:
        return len(self.items)

    @property
    def overdue_count(self) -> int:
        today = datetime.date.today()
        return sum(1 for it in self.items if it.due_date < today)

    @property
    def custodian_summary(self):
        counts = {}
        for it in self.items:
            name = it.custodian
            counts[name] = counts.get(name, 0) + 1
        return dict(sorted(counts.items()))

    def to_markdown(self):
        lines = [
            f"# AssetDesk Audit Report",
            "",
            f"- **Total items checked out:** {self.total_items}",
            f"- **Overdue items:** {self.overdue_count}",
            "- **Items by custodian:**",
        ]
        for name, count in self.custodian_summary.items():
            lines.append(f"  - {name}: {count}")
        return "\n".join(lines)


# Example: create a report from the previous demo items and print it.
demo_items = [
    Item("Laptop-A", "Alice", "2024-12-31", "Good"),
    Item("Monitor-B", "Bob", "2025-01-15", "Scratched screen"),
]

report = AssetDeskReport(demo_items)
print(report.to_markdown())
