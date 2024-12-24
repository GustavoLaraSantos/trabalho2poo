import json
import os

class Items:
    def __init__(self, filename):
        self.filename = filename
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file)

    def _load_items(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def _save_items(self, items):
        with open(self.filename, "w") as file:
            json.dump(items, file, indent=4)

    def create_item(self, name, quantity):
        items = self._load_items()
        if any(item['name'] == name for item in items):
            raise ValueError(f"Item with name '{name}' already exists.")
        items.append({"name": name, "quantity": quantity})
        self._save_items(items)

    def read_item(self, name):
        items = self._load_items()
        for item in items:
            if item['name'] == name:
                return item
        raise ValueError(f"Item with name '{name}' not found.")

    def update_item(self, name, quantity):
        items = self._load_items()
        for item in items:
            if item['name'] == name:
                item['quantity'] = quantity
                self._save_items(items)
                return
        raise ValueError(f"Item with name '{name}' not found.")

    def delete_item(self, name):
        items = self._load_items()
        filtered_items = [item for item in items if item['name'] != name]
        if len(filtered_items) == len(items):
            raise ValueError(f"Item with name '{name}' not found.")
        self._save_items(filtered_items)

    def list_items(self):
        return self._load_items()