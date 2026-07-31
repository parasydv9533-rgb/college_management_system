import tkinter as tk
from tkinter import messagebox

from controller.user_controller import UserController


class CreateAccount:

    def __init__(self):

        self.controller = UserController()

        self.root = tk.Toplevel()

        self.root.title("Create Account")
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f8ff")
        self.root.resizable(True,True)

        self.create_widgets()

    def create_widgets(self):

        tk.Label(
            self.root,
            text="CREATE ACCOUNT",
            bg="#f0f8ff",
            fg="#003366",
            font=("Arial",18,"bold")
        ).pack(pady=20)

       

        tk.Label(
            self.root,
            text="Username",
            bg="#f0f8ff",
            font=("Arial",12)
        ).pack()

        self.username = tk.Entry(
            self.root,
            width=30,
            font=("Arial",12)
        )
        self.username.pack(pady=5)

        tk.Label(
            self.root,
            text="Password",
            bg="#f0f8ff",
            font=("Arial",12)
        ).pack()

        self.password = tk.Entry(
            self.root,
            show="*",
            width=30,
            font=("Arial",12)
        )
        self.password.pack(pady=5)

        tk.Label(
            self.root,
            text="Confirm Password",
            bg="#f0f8ff",
            font=("Arial",12)
        ).pack()

        self.confirm = tk.Entry(
            self.root,
            show="*",
            width=30,
            font=("Arial",12)
        )
        self.confirm.pack(pady=5)

        tk.Button(
            self.root,
            text="Create Account",
            bg="#007bff",
            fg="white",
            width=20,
            font=("Arial",12,"bold"),
            cursor="hand2",
            command=self.create_account
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Close",
            bg="red",
            fg="white",
            width=20,
            font=("Arial",12,"bold"),
            cursor="hand2",
            command=self.root.destroy
        ).pack()

    def create_account(self):
    
        username = self.username.get().strip()
        password = self.password.get().strip()
        confirm = self.confirm.get().strip()

        if username == "" or password == "" or confirm == "":

            messagebox.showerror(
                "Error",
                "All fields are required."
            )
            return

        if password != confirm:

            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return
        try:

            # Check Username
            existing_user = self.controller.check_username(username)

            if existing_user:

                messagebox.showerror(
                    "Error",
                    "Username already exists.\nPlease choose another username."
                )
                return

            # Save User
            self.controller.save_user(
                username,
                password,
                "Admin"
            )

            messagebox.showinfo(
                "Success",
                "Account Created Successfully."
            )

            self.root.destroy()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )
