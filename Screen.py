import tkinter as tk
from abc import ABC, abstractmethod
from ItemsSystem import ItemsSystem

class Screen(ABC):
    @abstractmethod
    def __init__(self, root):
        self.root = root
        self.root.title()
        self.items_system = ItemsSystem('items.json')

    @abstractmethod
    def screen_config(self):
        pass

    @abstractmethod
    def display(self):
        pass