# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: AssetDesk
from datetime import datetime, timedelta
import json
import os
import shutil

ARCHIVE_DIR = "archive"
RETENTION_DAYS = 365

def archive_old_records(db_path):
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    
    cutoff_date = datetime.now() - timedelta(days=RETENTION_DAYS)
    archived_count = 0
    
    with open(db_path, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        
        new_lines = []
        for line in lines:
            if not line.strip():
                new_lines.append(line)
                continue
                
            try:
                data = json.loads(line)
                due_date_str = data.get('due_date', '')
                
                # Skip items without a due date or already archived
                if not due_date_str or 'archived' in data:
                    new_lines.append(line)
                    continue
                    
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                
                if due_date < cutoff_date and not data.get('archived', False):
                    # Archive the record
                    data['archived'] = True
                    data['archive_date'] = datetime.now().isoformat()
                    
                    archive_path = os.path.join(ARCHIVE_DIR, f"{data['id']}.json")
                    with open(archive_path, 'w', encoding='utf-8') as af:
                        json.dump(data, af)
                        
                    archived_count += 1
                    
                new_lines.append(json.dumps(data, ensure_ascii=False)) + '\n'
            except json.JSONDecodeError:
                # Keep invalid lines as is (or skip if desired)
                pass
                
        f.seek(0)
        f.truncate()
        f.writelines(new_lines)
        
    return archived_count

def restore_record(record_id, db_path):
    archive_file = os.path.join(ARCHIVE_DIR, f"{record_id}.json")
    
    if not os.path.exists(archive_file):
        print(f"Record {record_id} not found in archive.")
        return False
        
    with open(archive_file, 'r', encoding='utf-8') as af:
        data = json.load(af)
        
    # Remove archived flag to restore active status
    if 'archived' in data:
        del data['archived']
        if 'archive_date' in data:
            del data['archive_date']
            
    with open(db_path, 'w', encoding='utf-8') as f:
        for line in f.readlines():
            try:
                item = json.loads(line)
                if str(item.get('id')) == record_id:
                    continue # Skip the old archived entry in main DB
                f.write(line)
            except json.JSONDecodeError:
                pass
                
    with open(db_path, 'a', encoding='utf-8') as af:
        af.write(json.dumps(data, ensure_ascii=False) + '\n')
        
    return True
