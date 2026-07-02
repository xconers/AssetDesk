# === Stage 22: Add favorite records and quick favorite listing ===
# Project: AssetDesk
from typing import Optional, List
import json
from datetime import date

class FavoriteManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._favorites: dict[str, int] = {}  # item_id -> favorite_index
    
    def load_favorites(self) -> None:
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, list):
                for idx, record in enumerate(data):
                    self._favorites[record['id']] = idx
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    
    def add_favorite(self, item_id: str, note: Optional[str] = None) -> int:
        if item_id not in self._favorites:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            new_idx = len(data)
            record = {'id': item_id, 'note': note}
            data.append(record)
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self._favorites[item_id] = new_idx
            return new_idx
        return -1
    
    def get_favorites_list(self) -> List[dict]:
        with open(self.db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        favorites = []
        for idx in sorted(self._favorites.values()):
            if idx < len(data):
                item = data[idx]
                item['favorite_note'] = self._favorites.get(item['id'], '')
                favorites.append(item)
        return favorites
    
    def remove_favorite(self, item_id: str) -> bool:
        if item_id in self._favorites:
            del self._favorites[item_id]
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            try:
                idx = data.index({'id': item_id})
                data.pop(idx)
                with open(self.db_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                return True
            except ValueError:
                pass
        return False
