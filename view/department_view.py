
import tkinter as tk
from tkinter import ttk

from controller.department_controller import DepartmentController


class DepartmentView:

    def __init__(self):

        self.controller = DepartmentController()

        self.window = tk.Toplevel()

        self.window.title("Department Management")

        self.window.geometry("800x550")

        self.create_widgets()

        self.show_departments()

    def create_widgets(self):

        tk.Label(
            self.window,
            text="Department Management",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        # Department ID

        tk.Label(
            form,
            text="Department ID"
        ).grid(row=0,column=0,padx=10,pady=5)

        self.department_id = tk.Entry(form)

        self.department_id.grid(row=0,column=1)

        # Department Name

        tk.Label(
            form,
            text="Department Name"
        ).grid(row=1,column=0,padx=10,pady=5)

        self.department_name = tk.Entry(form,width=30)

        self.department_name.grid(row=1,column=1)

        # HOD Name

        tk.Label(
            form,
            text="HOD Name"
        ).grid(row=2,column=0,padx=10,pady=5)

        self.hod_name = tk.Entry(form,width=30)

        self.hod_name.grid(row=2,column=1)

                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Save",
            width=12,
            command=self.save_department
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            command=self.update_department
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            command=self.delete_department
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            command=self.search_department
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=12,
            command=self.show_departments
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            command=self.clear_fields
        ).grid(row=0, column=5, padx=5)

        

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

                "Department ID",
                "Department Name",
                "HOD Name"

            ),

            show="headings",

            yscrollcommand=scroll.set

        )

        scroll.config(command=self.tree.yview)

        self.tree.heading("Department ID", text="Department ID")
        self.tree.heading("Department Name", text="Department Name")
        self.tree.heading("HOD Name", text="HOD Name")

        self.tree.column("Department ID", width=120)
        self.tree.column("Department Name", width=250)
        self.tree.column("HOD Name", width=250)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

            # ==========================
    # Save Department
    # ==========================

    def save_department(self):

        self.controller.save_department(

            self.department_name.get(),
            self.hod_name.get()

        )

        self.clear_fields()

        self.show_departments()

    # ==========================
    # Update Department
    # ==========================

    def update_department(self):

        self.controller.update_department(

            self.department_id.get(),
            self.department_name.get(),
            self.hod_name.get()

        )

        self.clear_fields()

        self.show_departments()

    # ==========================
    # Delete Department
    # ==========================

    def delete_department(self):

        self.controller.delete_department(
            self.department_id.get()
        )

        self.clear_fields()

        self.show_departments()

        # ==========================
    # Search Department
    # ==========================

    def search_department(self):

        row = self.controller.search_department(
            self.department_id.get()
        )

        if row:

            self.clear_fields()

            self.department_id.insert(0, row[0])
            self.department_name.insert(0, row[1])
            self.hod_name.insert(0, row[2])

    # ==========================
    # Show All Departments
    # ==========================

    def show_departments(self):

        print(hasattr(self, "tree"))

        self.tree.delete(*self.tree.get_children())

        rows = self.controller.get_all_departments()

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    # ==========================
    # Select Record
    # ==========================

    def select_record(self, event):

        selected = self.tree.focus()

        values = self.tree.item(selected, "values")

        if values:

            self.clear_fields()

            self.department_id.insert(0, values[0])
            self.department_name.insert(0, values[1])
            self.hod_name.insert(0, values[2])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

        self.department_id.delete(0, tk.END)
        self.department_name.delete(0, tk.END)
        self.hod_name.delete(0, tk.END)