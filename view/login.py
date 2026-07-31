
import tkinter as tk
from tkinter import messagebox

from controller.user_controller import UserController
from view.dashboard import Dashboard


class Login:

    def __init__(self):

        self.controller = UserController()

        self.root = tk.Tk()

        self.root.title("College Management System")
        self.root.geometry("500x450")
        self.root.configure(bg="#f0f8ff")
        self.root.resizable(True,True)

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="COLLEGE MANAGEMENT SYSTEM",
            bg="#f0f8ff",
            fg="#003366",
            font=("Arial", 18, "bold")
        )

        title.pack(pady=25)

        tk.Label(
            self.root,
            text="Username",
            bg="#f0f8ff",
            font=("Arial", 12)
        ).pack()

        self.username = tk.Entry(
            self.root,
            font=("Arial",12),
            width=30
        )

        self.username.pack(pady=8)

        tk.Label(
            self.root,
            text="Password",
            bg="#f0f8ff",
            font=("Arial",12)
        ).pack()

        self.password = tk.Entry(
            self.root,
            show="*",
            font=("Arial",12),
            width=30
        )

        self.password.pack(pady=8)

        tk.Button(
            self.root,
            text="LOGIN",
            bg="#28a745",
            fg="white",
            activebackground="#218838",
            activeforeground="white",
            font=("Arial",12,"bold"),
            width=20,
            cursor="hand2",
            command=self.login
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="EXIT",
            bg="#dc3545",
            fg="white",
            activebackground="#c82333",
            activeforeground="white",
            font=("Arial",12,"bold"),
            width=20,
            cursor="hand2",
            command=self.root.destroy
        ).pack()

        tk.Button(
            self.root,
            text="Forgot Password?",
            fg="blue",
            bg="#f0f8ff",
            bd=0,
            cursor="hand2",
            font=("Arial",11,"underline"),
            command=self.open_forgot_password
        ).pack()

        tk.Button(
            self.root,
            text="Create Account",
            bg="#007bff",
            fg="white",
            width=20,
            font=("Arial", 12, "bold"),
            command=self.open_create_account
        ).pack(pady=5)

    # ==========================
    # Login
    # ==========================

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if not username or not password:
            messagebox.showerror(
                "Error",
                "Please Enter Username and Password"
            )
            return

        user = self.controller.login(username, password)

        if user:
            messagebox.showinfo(
                "Success",
                f"Welcome {user[1]}"
            )

            self.root.destroy()
            Dashboard()

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )

    
    # ==========================
    # Forgot Password
    # ==========================

    def open_forgot_password(self):

        from view.forgot_password import ForgotPassword

        ForgotPassword()


    def open_create_account(self):

        from view.create_account import CreateAccount

        CreateAccount()