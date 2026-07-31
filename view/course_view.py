
import tkinter as tk
from tkinter import ttk

from controller.course_controller import CourseController


class CourseView:

    def __init__(self):

        self.controller = CourseController()

        self.window = tk.Toplevel()

        self.window.title("Course Management")

        self.window.geometry("850x550")

        self.create_widgets()

        self.show_courses()

    def create_widgets(self):

        tk.Label(
            self.window,
            text="Course Management",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        # Course ID

        tk.Label(
            form,
            text="Course ID"
        ).grid(row=0,column=0,padx=10,pady=5)

        self.course_id = tk.Entry(form)

        self.course_id.grid(row=0,column=1)

        # Student ID

        tk.Label(
            form,
            text="Student ID"
        ).grid(row=0,column=2,padx=10)

        self.student_id = tk.Entry(form)

        self.student_id.grid(row=0,column=3)

        # Course Name
# ==========================
# Course Name
# ==========================

        tk.Label(
            form,
            text="Course Name"
        ).grid(row=1, column=0, padx=10, pady=5)

        self.course_name = tk.Entry(form)

        self.course_name.grid(row=1, column=1)

        # ==========================
        # Duration
        # ==========================

        tk.Label(
            form,
            text="Duration"
        ).grid(row=1, column=2, padx=10)

        self.duration = tk.Entry(form)

        self.duration.grid(row=1, column=3)

        # ==========================
        # Total Fee
        # ==========================

        tk.Label(
            form,
            text="Total Fee"
        ).grid(row=2, column=0, padx=10, pady=5)

        self.total_fee = tk.Entry(form)

        self.total_fee.grid(row=2, column=1)
                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Save",
            width=12,
            command=self.save_course
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            command=self.update_course
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            command=self.delete_course
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            command=self.search_course
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=12,
            command=self.show_courses
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

                "Course ID",
                "Course Name",
                "Duration",
                "Total Fee"


            ),

            show="headings",

            yscrollcommand=scroll.set

        )

        scroll.config(command=self.tree.yview)
        self.tree.heading("Course ID", text="Course ID")
        self.tree.heading("Course Name", text="Course Name")
        self.tree.heading("Duration", text="Duration")
        self.tree.heading("Total Fee", text="Total Fee")

        self.tree.column("Course ID", width=100)
        self.tree.column("Course Name", width=180)
        self.tree.column("Duration", width=180)
        self.tree.column("Total Fee", width=150)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

            # ==========================
    # Save Course
    # ==========================

    def save_course(self):

        self.controller.save_course(

        self.course_name.get(),
        self.duration.get(),
        self.total_fee.get()

    )

        self.clear_fields()

        self.show_courses()
     # ==========================
    # Update Course
    # ==========================

    def update_course(self):

        self.controller.update_course(

            self.course_id.get(),
            self.course_name.get(),
            self.duration.get(),
            self.total_fee.get()

        )

        self.clear_fields()

        self.show_courses()

    # ==========================
    # Delete Course
    # ==========================

    def delete_course(self):

        self.controller.delete_course(
            self.course_id.get()
        )

        self.clear_fields()

        self.show_courses()

        # ==========================
    # Search Course
    # ==========================

    def search_course(self):

        row = self.controller.search_course(
            self.course_id.get()
        )

        if row:

            self.clear_fields()
            self.course_id.insert(0, row[0])
            self.course_name.insert(0, row[1])
            self.duration.insert(0, row[2])
            self.total_fee.insert(0, row[3])

    # ==========================
    # Show All Courses
    # ==========================

    def show_courses(self):

        self.tree.delete(*self.tree.get_children())

        rows = self.controller.get_all_courses()

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

        self.course_id.insert(0, values[0])
        self.course_name.insert(0, values[1])
        self.duration.insert(0, values[2])
        self.total_fee.insert(0, values[3])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

       def clear_fields(self):

        self.course_id.delete(0, tk.END)
        self.course_name.delete(0, tk.END)
        self.duration.delete(0, tk.END)
        self.total_fee.delete(0, tk.END)
