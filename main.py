import tkinter as tk
from LoginScreen import LoginScreen

def main():
    root = tk.Tk()
    app = LoginScreen(root)
    app.display()

main()
