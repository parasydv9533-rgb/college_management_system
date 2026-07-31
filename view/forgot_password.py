import tkinter as tk
from tkinter import messagebox

from controller.user_controller import UserController


class ForgotPassword:

    def __init__(self):

        self.controller = UserController()

        self.root = tk.Toplevel()

        self.root.title("Forgot Password")
        self.root.geometry("400x350")

        tk.Label(
            self.root,
            text="Username"
        ).pack(pady=5)

        self.username = tk.Entry(self.root,width=30)
        self.username.pack()

        tk.Label(
            self.root,
            text="New Password"
        ).pack(pady=5)

        self.password = tk.Entry(
            self.root,
            show="*",
            width=30
        )

        self.password.pack()

        tk.Label(
            self.root,
            text="Confirm Password"
        ).pack(pady=5)

        self.confirm = tk.Entry(
            self.root,
            show="*",
            width=30
        )

        self.confirm.pack()

        tk.Button(
            self.root,
            text="Reset Password",
            command=self.reset_password
        ).pack(pady=20)

    def reset_password(self):

        username=self.username.get().strip()
        password=self.password.get().strip()
        confirm=self.confirm.get().strip()

        if username=="" or password=="" or confirm=="":
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        if password!=confirm:
            messagebox.showerror(
                "Error",
                "Passwords do not match"
            )
            return

        result=self.controller.reset_password(
            username,
            password
        )

        if result:

            messagebox.showinfo(
                "Success",
                "Password Updated Successfully"
            )

            self.root.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Username Not Found"
            )