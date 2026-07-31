
import tkinter as tk
from tkinter import ttk, messagebox

from controller.student_controller import StudentController


class StudentView:

    def __init__(self):

        self.controller = StudentController()

        self.root = tk.Toplevel()

        self.root.title("Student Management")
        self.root.geometry("1100x650")
        self.root.resizable(True, True)

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Student Management",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        form = tk.Frame(self.root)
        form.pack(pady=10)

        # ==========================
        # Row 0
        # ==========================

        tk.Label(form, text="Student ID").grid(row=0, column=0, padx=10, pady=5)

        self.student_id = tk.Entry(form, width=25)
        self.student_id.grid(row=0, column=1)

        tk.Label(form, text="First Name").grid(row=0, column=2, padx=10)

        self.first_name = tk.Entry(form, width=25)
        self.first_name.grid(row=0, column=3)

        # ==========================
        # Row 1
        # ==========================

        tk.Label(form, text="Last Name").grid(row=1, column=0, padx=10, pady=5)

        self.last_name = tk.Entry(form, width=25)
        self.last_name.grid(row=1, column=1)

        tk.Label(form, text="Gender").grid(row=1, column=2)

        self.gender = ttk.Combobox(
            form,
            values=["Male", "Female", "Other"],
            width=22,
            state="readonly"
        )

        self.gender.grid(row=1, column=3)

        # ==========================
        # Row 2
        # ==========================

        tk.Label(form, text="Date of Birth").grid(row=2, column=0)

        self.dob = tk.Entry(form, width=25)
        self.dob.grid(row=2, column=1)

        tk.Label(form, text="Phone").grid(row=2, column=2)

        self.phone = tk.Entry(form, width=25)
        self.phone.grid(row=2, column=3)

        # ==========================
        # Row 3
        # ==========================

        tk.Label(form, text="Email").grid(row=3, column=0)

        self.email = tk.Entry(form, width=25)
        self.email.grid(row=3, column=1)

        tk.Label(form, text="Address").grid(row=3, column=2)

        self.address = tk.Entry(form, width=25)
        self.address.grid(row=3, column=3)

        # ==========================
        # Row 4
        # ==========================

        tk.Label(form, text="Department ID").grid(row=4, column=0)

        self.department_id = tk.Entry(form, width=25)
        self.department_id.grid(row=4, column=1)

                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Save",
            width=15,
            command=self.save_student
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=15,
            command=self.update_student
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=15,
            command=self.delete_student
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=15,
            command=self.search_student
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=15,
            command=self.show_students
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=15,
            command=self.clear_fields
        ).grid(row=0, column=5, padx=5)

        

      

        # ==========================
        # TreeView
        # ==========================

        columns = (
            "ID",
            "First Name",
            "Last Name",
            "Gender",
            "DOB",
            "Phone",
            "Email",
            "Address",
            "Department"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

        self.show_students()

            # ==========================
    # Save Student
    # ==========================

    def save_student(self):

        try:

            if self.first_name.get() == "":
                messagebox.showerror("Error", "First Name is Required")
                return

            self.controller.save_student(
                self.first_name.get(),
                self.last_name.get(),
                self.gender.get(),
                self.dob.get(),
                self.phone.get(),
                self.email.get(),
                self.address.get(),
                self.department_id.get()
            )

            messagebox.showinfo("Success", "Student Saved Successfully")

            self.clear_fields()
            self.show_students()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ==========================
    # Update Student
    # ==========================

    def update_student(self):

        try:

            self.controller.update_student(
                self.student_id.get(),
                self.first_name.get(),
                self.last_name.get(),
                self.gender.get(),
                self.dob.get(),
                self.phone.get(),
                self.email.get(),
                self.address.get(),
                self.department_id.get()
            )

            messagebox.showinfo("Success", "Student Updated Successfully")

            self.clear_fields()
            self.show_students()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ==========================
    # Delete Student
    # ==========================

    def delete_student(self):

        try:

            if self.student_id.get() == "":
                messagebox.showerror("Error", "Select Student")
                return

            self.controller.delete_student(
                self.student_id.get()
            )

            messagebox.showinfo("Success", "Student Deleted Successfully")

            self.clear_fields()
            self.show_students()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # ==========================
    # Search Student
    # ==========================

    def search_student(self):

        try:

            if self.student_id.get() == "":
                messagebox.showerror("Error", "Enter Student ID")
                return

            row = self.controller.search_student(
                self.student_id.get()
            )

            if row:

                self.clear_fields()

                self.student_id.insert(0, row[0])
                self.first_name.insert(0, row[1])
                self.last_name.insert(0, row[2])

                self.gender.set(row[3])

                self.dob.insert(0, row[4])
                self.phone.insert(0, row[5])
                self.email.insert(0, row[6])
                self.address.insert(0, row[7])
                self.department_id.insert(0, row[8])

            else:

                messagebox.showinfo(
                    "Not Found",
                    "Student Not Found"
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================
    # Show Students
    # ==========================

    def show_students(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = self.controller.get_all_students()

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    # ==========================
    # TreeView Selection
    # ==========================

    def select_record(self, event):

        selected = self.tree.focus()

        if selected == "":
            return

        values = self.tree.item(selected, "values")

        self.clear_fields()

        self.student_id.insert(0, values[0])
        self.first_name.insert(0, values[1])
        self.last_name.insert(0, values[2])

        self.gender.set(values[3])

        self.dob.insert(0, values[4])
        self.phone.insert(0, values[5])
        self.email.insert(0, values[6])
        self.address.insert(0, values[7])
        self.department_id.insert(0, values[8])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

        self.student_id.delete(0, tk.END)
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)

        self.gender.set("")

        self.dob.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.department_id.delete(0, tk.END)
