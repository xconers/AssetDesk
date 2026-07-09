# === Stage 41: Add plain text import for a simple line-based format ===
# Project: AssetDesk
def import_lines(filename):
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 5:
                item = {
                    'id': int(parts[0]),
                    'name': parts[1],
                    'custodian': parts[2].strip(),
                    'due_date': parts[3],
                    'condition': parts[4]
                }
                if len(parts) >= 6:
                    item['notes'] = parts[5]
                else:
                    item['notes'] = ''
                items.append(item)
    return items
