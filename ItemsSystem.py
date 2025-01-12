import json
import os

class ItemsSystem:
    def __init__(self, filename):
        self.filename = filename
        self.__ensure_file()

    def __ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file)

    def __load_items(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def __save_items(self, items):
        with open(self.filename, "w") as file:
            json.dump(items, file, indent=4)

    def create_item(self, name, quantity):
        items = self.__load_items()
        if any(item['name'] == name for item in items):
            return {
                'status': 400,
                'statusMessage': f"O item com o nome '{name}' já existe.",
                'data': {}
            }
        new_item = {"name": name, "quantity": quantity}
        items.append(new_item)
        self.__save_items(items)
        return {
            'status': 201,
            'statusMessage': f"O item com o nome '{name}' foi criado com sucesso.",
            'data': new_item
        }

    def read_item(self, name):
        items = self.__load_items()
        for item in items:
            if item['name'] == name:
                return {
                    'status': 200,
                    'statusMessage': f"O item com o nome '{name}' foi encontrado.",
                    'data': item
                }
        return {
            'status': 404,
            'statusMessage': f"O item com o nome '{name}' não foi encontrado.",
            'data': {}
        }

    def update_item(self, name, quantity):
        items = self.__load_items()
        for item in items:
            if item['name'] == name:
                item['quantity'] = quantity
                self.__save_items(items)
                return {
                    'status': 200,
                    'statusMessage': f"O item com o nome '{name}' foi atualizado.",
                    'data': {"name": name, "quantity": quantity}
                }
        return {
            'status': 404,
            'statusMessage': f"O item com o nome '{name}' não foi encontrado.",
            'data': {}
        }

    def delete_item(self, name):
        items = self.__load_items()
        filtered_items = [item for item in items if item['name'] != name]
        if len(filtered_items) == len(items):
            return {
                'status': 404,
                'statusMessage': f"O item com o nome '{name}' não foi encontrado.",
                'data': {}
            }
        self.__save_items(filtered_items)
        return {
            'status': 200,
            'statusMessage': f"O item com o nome '{name}' foi deletado com sucesso.",
            'data': {}
        }

    def list_items(self):
        return {
            'status': 200,
            'statusMessage': f"Todos os itens foram encontrados.",
            'data': self.__load_items()
        }