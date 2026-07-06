# === Stage 32: Add pagination helpers for long console output ===
# Project: AssetDesk
def print_table(headers, rows, col_widths=None):
    if not headers:
        return
    widths = [len(str(h)) for h in headers]
    if col_widths is None and len(rows) > 0:
        for row in rows:
            for i, val in enumerate(row):
                widths[i] = max(widths[i], len(str(val)))
    header_str = " | ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers))
    print(header_str)
    sep = "-+-".join("-" * w for w in widths)
    print(sep)
    for row in rows:
        line = " | ".join(str(v).ljust(widths[i]) if v is not None else str(v).rjust(widths[i]) for i, v in enumerate(row))
        print(line)

def paginate(lines, page_size=20):
    total_pages = (len(lines) + page_size - 1) // page_size
    for i in range(total_pages):
        start = i * page_size
        end = min((i + 1) * page_size, len(lines))
        print(f"\n--- Page {i+1}/{total_pages} ---")
        for line in lines[start:end]:
            print(line)

def format_number(n):
    if n is None:
        return "-"
    return f"{n:,}"
