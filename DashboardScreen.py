import tkinter as tk
from tkinter import messagebox, simpledialog
from Screen import Screen
from ItemsSystem import ItemsSystem
from AddProductScreen import AddProductScreen

class DashboardScreen(Screen):
    def __init__(self, root):
        super().__init__(root)
        self.items = self.items_system.list_items()['data']
        self.screen_config()

    def screen_config(self):
        self.root.geometry("600x500")
        self.root.title("Dashboard")
        self.root.configure(bg="#1e1e1e")

        header_frame = tk.Frame(self.root, bg="#3e3e3e", height=50)
        header_frame.pack(fill="x")

        welcome_label = tk.Label(header_frame, text="Bem vindo", font=("Arial", 16), bg="#3e3e3e", fg="#ffffff")
        welcome_label.pack(side="left", padx=20)

        logout_button = tk.Button(header_frame, text="Sair", font=("Arial", 12), command=self.logout, bg="#ff4d4d", fg="#ffffff", cursor="hand2")
        logout_button.pack(side="right", padx=20, pady=10)

        body_frame = tk.Frame(self.root, bg="#1e1e1e")
        body_frame.pack(fill="both", expand=True, padx=20, pady=20)

        stock_frame = tk.Frame(body_frame, bg="#1e1e1e")
        stock_frame.pack(fill="x")

        stock_label = tk.Label(stock_frame, text="Estoque", font=("Arial", 18), bg="#1e1e1e", fg="#ffffff")
        stock_label.pack(side="left")

        add_button = tk.Button(stock_frame, text="Adicionar Produto", font=("Arial", 12), command=self.add_product, bg="#3e3e3e", fg="#ffffff", cursor="hand2")
        add_button.pack(side="right")

        self.items_frame = tk.Frame(body_frame, bg="#1e1e1e")
        self.items_frame.pack(fill="both", expand=True, pady=10)
        self.render_items()

    def render_items(self):
        for widget in self.items_frame.winfo_children():
            widget.destroy()

        for item in self.items:
            item_frame = tk.Frame(self.items_frame, bg="#2e2e2e", bd=2, relief="solid")
            item_frame.pack(fill="x", pady=5)

            item_label = tk.Label(item_frame, text=item["name"], font=("Arial", 14), bg="#2e2e2e", fg="#ffffff")
            item_label.pack(side="left", padx=10)

            delete_button = tk.Button(
                item_frame,
                text="🗑",
                font=("Arial", 12),
                command=lambda i=item: self.delete_item(i),
                bg="#ff4d4d",
                fg="#ffffff",
                cursor="hand2",
            )
            delete_button.pack(side="right", padx=10, pady=10)

            decrement_button = tk.Button(
                item_frame,
                text="-",
                font=("Arial", 12),
                command=lambda i=item: self.change_quantity(i, -1),
                bg="#3e3e3e",
                fg="#ffffff",
                cursor="hand2",
                width=1
            )
            decrement_button.pack(side="right", padx=(5, 20), pady=15)

            quantity_value = tk.Label(
                item_frame,
                text=str(item["quantity"]),
                font=("Arial", 14),
                bg="#2e2e2e",
                fg="#ffffff",
                cursor="hand2",
            )
            quantity_value.pack(side="right")
            quantity_value.bind("<Button-1>", lambda e, i=item: self.set_quantity(i))

            increment_button = tk.Button(
                item_frame,
                text="+",
                font=("Arial", 12),
                command=lambda i=item: self.change_quantity(i, 1),
                bg="#3e3e3e",
                fg="#ffffff",
                cursor="hand2",
                width=1
            )
            increment_button.pack(side="right", padx=5, pady=15)

    def change_quantity(self, item, delta):
        new_quantity = item["quantity"] + delta
        if new_quantity < 0:
            new_quantity = 0
        self.update_quantity(item, new_quantity)
        
    

    def set_quantity(self, item):
        new_quantity = simpledialog.askinteger("Alterar Quantidade", f"Digite a nova quantidade para {item['name']}", minvalue=0)
        if new_quantity is not None:
            self.update_quantity(item, new_quantity)

    def update_quantity(self, item, new_quantity):
        response = self.items_system.update_item(item["name"], new_quantity)

        if response["status"] == 200:
            item["quantity"] = new_quantity
            self.render_items()
        else:
            messagebox.showerror("Erro", response["statusMessage"])

    def delete_item(self, item):
        response = self.items_system.delete_item(item['name'])
        if (response['status'] == 200):
            self.items.remove(item)
            self.render_items()
        else:
            messagebox.showerror("Erro", response["statusMessage"])

    def add_product(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        add_product_screen = AddProductScreen(self.root)
        add_product_screen.display()

    def logout(self):
        from LoginScreen import LoginScreen
        for widget in self.root.winfo_children():
            widget.destroy()
        login_screen = LoginScreen(self.root)
        login_screen.display()

    def display(self):
        self.root.mainloop()