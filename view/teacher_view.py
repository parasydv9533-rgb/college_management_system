
import tkinter as tk
from tkinter import ttk

from controller.teacher_controller import TeacherController


class TeacherView:

    def __init__(self):

        self.controller = TeacherController()

        self.window = tk.Toplevel()

        self.window.title("Teacher Management")

        self.window.geometry("900x600")

        self.create_widgets()

        self.show_teachers()

    def create_widgets(self):

        tk.Label(
            self.window,
            text="Teacher Management",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        # Teacher ID

        tk.Label(form,text="Teacher ID").grid(row=0,column=0,padx=10,pady=5)

        self.teacher_id = tk.Entry(form)
        self.teacher_id.grid(row=0,column=1)

        # First Name

        tk.Label(form,text="First Name").grid(row=0,column=2,padx=10)

        self.first_name = tk.Entry(form)
        self.first_name.grid(row=0,column=3)

        # Last Name

        tk.Label(form,text="Last Name").grid(row=1,column=0,padx=10,pady=5)

        self.last_name = tk.Entry(form)
        self.last_name.grid(row=1,column=1)

        # Gender

        tk.Label(form,text="Gender").grid(row=1,column=2)

        self.gender = ttk.Combobox(
            form,
            values=["Male","Female","Other"],
            state="readonly",
            width=18
        )

        self.gender.grid(row=1,column=3)

        # Phone

        tk.Label(form,text="Phone").grid(row=2,column=0,padx=10,pady=5)

        self.phone = tk.Entry(form)
        self.phone.grid(row=2,column=1)

        # Email

        tk.Label(form,text="Email").grid(row=2,column=2)

        self.email = tk.Entry(form)
        self.email.grid(row=2,column=3)

        # Qualification

        tk.Label(form,text="Qualification").grid(row=3,column=0,padx=10,pady=5)

        self.qualification = tk.Entry(form)
        self.qualification.grid(row=3,column=1)

        # Salary

        tk.Label(form,text="Salary").grid(row=3,column=2)

        self.salary = tk.Entry(form)
        self.salary.grid(row=3,column=3)

        # Department ID

        tk.Label(form,text="Department ID").grid(row=4,column=0,padx=10,pady=5)

        self.department = tk.Entry(form)
        self.department.grid(row=4,column=1)

                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Save",
            width=12,
            command=self.save_teacher
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            command=self.update_teacher
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            command=self.delete_teacher
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            command=self.search_teacher
        ).grid(row=0,column=3,padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=12,
            command=self.show_teachers
        ).grid(row=0,column=4,padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            command=self.clear_fields
        ).grid(row=0,column=5,padx=5)

       

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

                "ID",
                "First Name",
                "Last Name",
                "Gender",
                "Phone",
                "Email",
                "Qualification",
                "Salary",
                "Department"

            ),

            show="headings",

            yscrollcommand=scroll.set

        )

        scroll.config(command=self.tree.yview)

        self.tree.heading("ID", text="ID")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Qualification", text="Qualification")
        self.tree.heading("Salary", text="Salary")
        self.tree.heading("Department", text="Department")

        self.tree.column("ID", width=70)
        self.tree.column("First Name", width=120)
        self.tree.column("Last Name", width=120)
        self.tree.column("Gender", width=80)
        self.tree.column("Phone", width=120)
        self.tree.column("Email", width=180)
        self.tree.column("Qualification", width=140)
        self.tree.column("Salary", width=100)
        self.tree.column("Department", width=100)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

            # ==========================
    # Save Teacher
    # ==========================

    def save_teacher(self):

        self.controller.save_teacher(

            self.first_name.get(),
            self.last_name.get(),
            self.gender.get(),
            self.phone.get(),
            self.email.get(),
            self.qualification.get(),
            self.salary.get(),
            self.department.get()

        )

        self.clear_fields()

        self.show_teachers()

    # ==========================
    # Update Teacher
    # ==========================

    def update_teacher(self):

        self.controller.update_teacher(

            self.teacher_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.gender.get(),
            self.phone.get(),
            self.email.get(),
            self.qualification.get(),
            self.salary.get(),
            self.department.get()

        )

        self.clear_fields()

        self.show_teachers()

    # ==========================
    # Delete Teacher
    # ==========================

    def delete_teacher(self):

        self.controller.delete_teacher(
            self.teacher_id.get()
        )

        self.clear_fields()

        self.show_teachers()

        # ==========================
    # Search Teacher
    # ==========================

    def search_teacher(self):

        row = self.controller.search_teacher(
            self.teacher_id.get()
        )

        if row:

            self.clear_fields()

            self.teacher_id.insert(0, row[0])
            self.first_name.insert(0, row[1])
            self.last_name.insert(0, row[2])
            self.gender.set(row[3])
            self.phone.insert(0, row[4])
            self.email.insert(0, row[5])
            self.qualification.insert(0, row[6])
            self.salary.insert(0, row[7])
            self.department.insert(0, row[8])

    # ==========================
    # Show All Teachers
    # ==========================

    def show_teachers(self):

        self.tree.delete(*self.tree.get_children())

        rows = self.controller.get_all_teachers()

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

            self.teacher_id.insert(0, values[0])
            self.first_name.insert(0, values[1])
            self.last_name.insert(0, values[2])
            self.gender.set(values[3])
            self.phone.insert(0, values[4])
            self.email.insert(0, values[5])
            self.qualification.insert(0, values[6])
            self.salary.insert(0, values[7])
            self.department.insert(0, values[8])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

        self.teacher_id.delete(0, tk.END)
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.gender.set("")
        self.phone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.qualification.delete(0, tk.END)
        self.salary.delete(0, tk.END)
        self.department.delete(0, tk.END)
