import tkinter as tk
from tkinter import messagebox
from Screen import Screen

class AddProductScreen(Screen):
    def __init__(self, root):
        super().__init__(root)
        self.screen_config()

    def screen_config(self):
        self.root.geometry("600x500")
        self.root.title("Adicionar novo produto")

        main_frame = tk.Frame(self.root, bg="#1e1e1e")
        main_frame.pack(fill="both", expand=True)

        back_button = tk.Button(main_frame, text="←", font=("Arial", 14), command=self.go_back, bg="#3e3e3e", fg="#ffffff", cursor="hand2")
        back_button.place(x=10, y=10)

        title_label = tk.Label(main_frame, text="Adicionar novo produto", font=("Arial", 18), bg="#1e1e1e", fg="#ffffff")
        title_label.pack(pady=(40, 20))

        form_frame = tk.Frame(main_frame, bg="#1e1e1e")
        form_frame.pack(pady=20)

        name_label = tk.Label(form_frame, text="Nome do Produto", font=("Arial", 14), bg="#1e1e1e", fg="#ffffff", anchor="w")
        name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.name_entry = tk.Entry(form_frame, font=("Arial", 14), bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", width=30)
        self.name_entry.grid(row=1, column=0, pady=(0, 20))

        quantity_label = tk.Label(form_frame, text="Quantidade", font=("Arial", 14), bg="#1e1e1e", fg="#ffffff", anchor="w")
        quantity_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.quantity_entry = tk.Entry(form_frame, font=("Arial", 14), bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", width=30)
        self.quantity_entry.grid(row=3, column=0, pady=(0, 20))

        add_button = tk.Button(main_frame, text="Adicionar", font=("Arial", 14), command=self.add_product, bg="#3e3e3e", fg="#ffffff", cursor="hand2")
        add_button.pack(pady=20)

    def add_product(self):
        name = self.name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if not name:
            messagebox.showerror("Erro", "O nome do produto não pode estar vazio.")
            return

        if not quantity.isdigit():
            messagebox.showerror("Erro", "A quantidade deve ser um número válido.")
            return

        response = self.items_system.create_item(name, int(quantity))

        if (response['status'] == 201):
            self.go_back()
        else:   
            messagebox.showinfo("Erro", response['statusMessage'])

    def go_back(self):
        from DashboardScreen import DashboardScreen
        for widget in self.root.winfo_children():
                widget.destroy()
        dashboard_screen = DashboardScreen(self.root)
        dashboard_screen.display()

    def display(self):
        self.root.mainloop()