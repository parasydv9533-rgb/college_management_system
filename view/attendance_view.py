
import tkinter as tk
from tkinter import ttk

from controller.attendance_controller import AttendanceController


class AttendanceView:

    def __init__(self):

        self.controller = AttendanceController()

        self.window = tk.Toplevel()

        self.window.title("Attendance Management")

        self.window.geometry("850x550")

        self.create_widgets()

        self.show_attendance()

    def create_widgets(self):

        tk.Label(
            self.window,
            text="Attendance Management",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        # Attendance ID

        tk.Label(
            form,
            text="Attendance ID"
        ).grid(row=0,column=0,padx=10,pady=5)

        self.attendance_id = tk.Entry(form)

        self.attendance_id.grid(row=0,column=1)

        # Student ID

        tk.Label(
            form,
            text="Student ID"
        ).grid(row=1,column=0,padx=10,pady=5)

        self.student_id = tk.Entry(form)

        self.student_id.grid(row=1,column=1)

        # Attendance Date

        tk.Label(
            form,
            text="Attendance Date"
        ).grid(row=2,column=0,padx=10,pady=5)

        self.attendance_date = tk.Entry(form)

        self.attendance_date.grid(row=2,column=1)

        # Status

        tk.Label(
            form,
            text="Status"
        ).grid(row=3,column=0,padx=10,pady=5)

        self.status = ttk.Combobox(
            form,
            values=["Present","Absent"],
            state="readonly",
            width=27
        )

        self.status.grid(row=3,column=1)

                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Save",
            width=12,
            command=self.save_attendance
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            command=self.update_attendance
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            command=self.delete_attendance
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            command=self.search_attendance
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=12,
            command=self.show_attendance
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

                "Attendance ID",
                "Student ID",
                "Attendance Date",
                "Status"

            ),

            show="headings",

            yscrollcommand=scroll.set

        )

        scroll.config(command=self.tree.yview)

        self.tree.heading("Attendance ID", text="Attendance ID")
        self.tree.heading("Student ID", text="Student ID")
        self.tree.heading("Attendance Date", text="Attendance Date")
        self.tree.heading("Status", text="Status")

        self.tree.column("Attendance ID", width=120)
        self.tree.column("Student ID", width=120)
        self.tree.column("Attendance Date", width=180)
        self.tree.column("Status", width=120)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

            # ==========================
    # Save Attendance
    # ==========================

    def save_attendance(self):

        self.controller.save_attendance(

            self.student_id.get(),
            self.attendance_date.get(),
            self.status.get()

        )

        self.clear_fields()

        self.show_attendance()

    # ==========================
    # Update Attendance
    # ==========================

    def update_attendance(self):

        self.controller.update_attendance(

            self.attendance_id.get(),
            self.student_id.get(),
            self.attendance_date.get(),
            self.status.get()

        )

        self.clear_fields()

        self.show_attendance()

    # ==========================
    # Delete Attendance
    # ==========================

    def delete_attendance(self):

        self.controller.delete_attendance(
            self.attendance_id.get()
        )

        self.clear_fields()

        self.show_attendance()

        # ==========================
    # Search Attendance
    # ==========================

    def search_attendance(self):

        row = self.controller.search_attendance(
            self.attendance_id.get()
        )

        if row:

            self.clear_fields()

            self.attendance_id.insert(0, row[0])
            self.student_id.insert(0, row[1])
            self.attendance_date.insert(0, row[2])
            self.status.set(row[3])

    # ==========================
    # Show All Attendance
    # ==========================

    def show_attendance(self):

        self.tree.delete(*self.tree.get_children())

        rows = self.controller.get_all_attendance()

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

            self.attendance_id.insert(0, values[0])
            self.student_id.insert(0, values[1])
            self.attendance_date.insert(0, values[2])
            self.status.set(values[3])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

        self.attendance_id.delete(0, tk.END)
        self.student_id.delete(0, tk.END)
        self.attendance_date.delete(0, tk.END)
        self.status.set("")