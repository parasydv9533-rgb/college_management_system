
import tkinter as tk
from tkinter import ttk

from controller.user_controller import UserController


class UserView:

    def __init__(self):

        self.controller = UserController()

        self.window = tk.Toplevel()

        self.window.title("User Management")

        self.window.geometry("800x550")

        self.create_widgets()

        self.show_users()

    def create_widgets(self):

        tk.Label(
            self.window,
            text="User Management",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        # User ID

        tk.Label(
            form,
            text="User ID"
        ).grid(row=0,column=0,padx=10,pady=5)

        self.user_id = tk.Entry(form)

        self.user_id.grid(row=0,column=1)

        # Username

        tk.Label(
            form,
            text="Username"
        ).grid(row=1,column=0,padx=10,pady=5)

        self.username = tk.Entry(form,width=30)

        self.username.grid(row=1,column=1)

        # Password

        tk.Label(
            form,
            text="Password"
        ).grid(row=2,column=0,padx=10,pady=5)

        self.password = tk.Entry(form,width=30,show="*")

        self.password.grid(row=2,column=1)

        # Role

        tk.Label(
            form,
            text="Role"
        ).grid(row=3,column=0,padx=10,pady=5)

        self.role = ttk.Combobox(
            form,
            values=["Admin","Staff"],
            state="readonly",
            width=27
        )

        self.role.grid(row=3,column=1)

                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Save",
            width=12,
            command=self.save_user
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            command=self.update_user
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            command=self.delete_user
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            command=self.search_user
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=12,
            command=self.show_users
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            command=self.clear_fields
        ).grid(row=0, column=5, padx=5)

        tk.Button(
            button_frame,
            text="Back_Dashboard",
            width=12,
            command=self.Back_Dashboard
        ).grid(row=0, column=6, padx=5)

        # ==========================
        # Table
        # ==========================

        table_frame = tk.Frame(self.window)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        scroll = tk.Scrollbar(table_frame)
        scroll.pack(side="right", fill="y")

        self.tree = ttk.Treeview(

            table_frame,

            columns=(

                "User ID",
                "Username",
                "Password",
                "Role"

            ),

            show="headings",

            yscrollcommand=scroll.set

        )

        scroll.config(command=self.tree.yview)

        self.tree.heading("User ID", text="User ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Role", text="Role")

        self.tree.column("User ID", width=100)
        self.tree.column("Username", width=200)
        self.tree.column("Password", width=200)
        self.tree.column("Role", width=120)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

            # ==========================
    # Save User
    # ==========================

    def save_user(self):

        self.controller.save_user(

        self.full_name.get(),
        self.username.get(),
        self.password.get(),
        self.role.get()

    )

        self.clear_fields()

        self.show_users()

    # ==========================
    # Update User
    # ==========================

    def update_user(self):

        self.controller.update_user(

            self.user_id.get(),
            self.username.get(),
            self.password.get(),
            self.role.get()

        )

        self.clear_fields()

        self.show_users()

    # ==========================
    # Delete User
    # ==========================

    def delete_user(self):

        self.controller.delete_user(
            self.user_id.get()
        )

        self.clear_fields()

        self.show_users()

        # ==========================
    # Search User
    # ==========================

    def search_user(self):

        row = self.controller.search_user(
            self.user_id.get()
        )

        if row:

            self.clear_fields()

            self.user_id.insert(0, row[0])
            self.username.insert(0, row[1])
            self.password.insert(0, row[2])
            self.role.set(row[3])

    # ==========================
    # Show All Users
    # ==========================

    def show_users(self):

        self.tree.delete(*self.tree.get_children())

        rows = self.controller.get_all_users()

        for row in rows:

            self.tree.insert(
                "",
                tk.END,
                values=row
            )

    # ==========================
    # Select Record
    # ==========================

    def select_record(self, event):

        selected = self.tree.focus()

        values = self.tree.item(selected, "values")

        if values:

            self.clear_fields()

            self.user_id.insert(0, values[0])
            self.username.insert(0, values[1])
            self.password.insert(0, values[2])
            self.role.set(values[3])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

        self.user_id.delete(0, tk.END)
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.role.set("")

    

    def Back_Dashboard(self):
        self.window.destroy()
        self.Dashboard()
