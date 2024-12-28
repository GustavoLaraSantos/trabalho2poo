import tkinter as tk
from tkinter import messagebox
from Screen import Screen
from DashboardScreen import DashboardScreen

class LoginScreen(Screen):
    def __init__(self, root):
        super().__init__(root)
        self.screen_config()

    def screen_config(self):
        self.root.geometry("600x500")
        self.root.title("Sistema de Gerenciamento de Componentes Elétricos")

        main_frame = tk.Frame(self.root, bg="#1e1e1e")
        main_frame.pack(fill="both", expand=True)

        title_label = tk.Label(main_frame, text="Sistema de Gerenciamento de\nComponentes Elétricos", font=("Arial", 18), wraplength=720, justify="center", bg="#1e1e1e", fg="#ffffff")
        title_label.pack(pady=(20, 40))

        input_frame = tk.Frame(main_frame, bg="#1e1e1e")
        input_frame.pack(pady=10)

        user_label = tk.Label(input_frame, text="Usuário", font=("Arial", 14), bg="#1e1e1e", fg="#ffffff", anchor="w")
        user_label.grid(row=0, column=0, sticky="w", padx=40, pady=(0, 5))
        self.user_entry = tk.Entry(input_frame, font=("Arial", 14), bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", width=30)
        self.user_entry.grid(row=1, column=0, padx=40, sticky="w")

        password_label = tk.Label(input_frame, text="Senha", font=("Arial", 14), bg="#1e1e1e", fg="#ffffff", anchor="w")
        password_label.grid(row=2, column=0, sticky="w", padx=40, pady=(20, 5))
        self.password_entry = tk.Entry(input_frame, font=("Arial", 14), show="*", bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff", width=30)
        self.password_entry.grid(row=3, column=0, padx=40, sticky="w")
        self.password_entry.bind("<Return>", lambda event: self.authenticate())

        login_button = tk.Button(main_frame, text="Entrar", font=("Arial", 14), command=self.authenticate, bg="#3e3e3e", fg="#ffffff", activebackground="#5e5e5e", activeforeground="#ffffff", cursor="hand2")
        login_button.pack(pady=30)

        exit_button = tk.Button(main_frame, text="Fechar", font=("Arial", 10), command=self.exit_app, bg="#ff4d4d", fg="#ffffff", activebackground="#ff6666", activeforeground="#ffffff", cursor="hand2")
        exit_button.place(relx=0.99, rely=0.99, anchor="se", x=-20, y=-20)

    def authenticate(self):
        user = self.user_entry.get().strip()
        password = self.password_entry.get().strip()

        if user == "admin" and password == "admin":
            for widget in self.root.winfo_children():
                widget.destroy()
            dashboard_screen = DashboardScreen(self.root)
            dashboard_screen.display()
        else:
            messagebox.showerror("Erro", "Usuário e/ou Senha incorretos")

    def exit_app(self):
        self.root.destroy()

    def display(self):
        self.root.mainloop()