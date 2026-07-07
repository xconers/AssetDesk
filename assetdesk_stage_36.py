# === Stage 36: Add templates for quickly creating common records ===
# Project: AssetDesk
class AssetTemplate:
    """Templates for quickly creating common records."""
    
    _templates = {
        'laptop': {'item_type': 'Electronics', 'category': 'Laptops'},
        'monitor': {'item_type': 'Electronics', 'category': 'Monitors'},
        'desk': {'item_type': 'Furniture', 'category': 'Desks'},
        'keyboard': {'item_type': 'Peripherals', 'category': 'Keyboards'},
        'mouse': {'item_type': 'Peripherals', 'category': 'Mice'},
    }

    @classmethod
    def get_template(cls, name):
        if name not in cls._templates:
            raise KeyError(f"Unknown template: {name}. Available: {list(cls._templates.keys())}")
        return dict(cls._templates[name])

    @classmethod
    def create_item_from_template(cls, name, custodian_id, due_date='2030-12-31', condition_note=None):
        item_data = cls.get_template(name)
        return {
            'item_type': item_data['item_type'],
            'category': item_data['category'],
            'custodian_id': custodian_id,
            'due_date': due_date,
            'condition_note': condition_note or 'New',
            'template_used': name,
        }

    @classmethod
    def register_template(cls, name, data):
        cls._templates[name] = data
