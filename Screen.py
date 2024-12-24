import tkinter as tk
from abc import ABC, abstractmethod
from Items import Items

class Screen(ABC):
    def __init__(self, root):
        self.root = root
        self.root.title()
        self.items = Items('items.json')

    @abstractmethod
    def screen_config(self):
        pass

    @abstractmethod
    def display(self):
        pass