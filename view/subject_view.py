
import tkinter as tk
from tkinter import ttk

from controller.subject_controller import SubjectController


class SubjectView:

    def __init__(self):

        self.controller = SubjectController()

        self.window = tk.Toplevel()

        self.window.title("Subject Management")

        self.window.geometry("900x700")

        self.create_widgets()

        self.show_subjects()

    def create_widgets(self):

        tk.Label(
            self.window,
            text="Subject Management",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        form = tk.Frame(self.window)
        form.pack()

        # Subject ID

        tk.Label(
            form,
            text="Subject ID"
        ).grid(row=0,column=0,padx=10,pady=5)

        self.subject_id = tk.Entry(form)

        self.subject_id.grid(row=0,column=1)

        # Subject Name

        tk.Label(
            form,
            text="Subject Name"
        ).grid(row=1,column=0,padx=10,pady=5)

        self.subject_name = tk.Entry(form,width=30)

        self.subject_name.grid(row=1,column=1)

        

        # Semester

        tk.Label(
            form,
            text="Semester"
        ).grid(row=3,column=0,padx=10,pady=5)

        self.semester = tk.Entry(form,width=30)

        self.semester.grid(row=3,column=1)

        # Course ID

        tk.Label(
            form,
            text="Course ID"
        ).grid(row=4,column=0,padx=10,pady=5)

        self.course_id = tk.Entry(form,width=30)

        self.course_id.grid(row=4,column=1)

                # ==========================
        # Buttons
        # ==========================

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Save",
            width=12,
            command=self.save_subject
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            command=self.update_subject
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            command=self.delete_subject
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            command=self.search_subject
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Show All",
            width=12,
            command=self.show_subjects
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
                "Subject ID",
                "Subject Name",
               
                "Semester",
                "Course ID"
            ),

            show="headings",

            yscrollcommand=scroll.set

        )

        scroll.config(command=self.tree.yview)

        self.tree.heading("Subject ID", text="Subject ID")
        self.tree.heading("Subject Name", text="Subject Name")
        
        self.tree.heading("Semester", text="Semester")
        self.tree.heading("Course ID", text="Course ID")

        self.tree.column("Subject ID", width=100)
        self.tree.column("Subject Name", width=220)
       
        self.tree.column("Semester", width=120)
        self.tree.column("Course ID", width=120)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

            # ==========================
    # Save Subject
    # ==========================

    def save_subject(self):

        self.controller.save_subject(
            self.subject_name.get(),
           
            self.semester.get(),
            self.course_id.get()
        )

        self.clear_fields()
        self.show_subjects()

    # ==========================
    # Update Subject
    # ==========================

    def update_subject(self):

        self.controller.update_subject(
            self.subject_id.get(),
            self.subject_name.get(),
            
            self.semester.get(),
            self.course_id.get()
        )

        self.clear_fields()
        self.show_subjects()

    # ==========================
    # Delete Subject
    # ==========================

    def delete_subject(self):

        self.controller.delete_subject(
            self.subject_id.get()
        )

        self.clear_fields()

        self.show_subjects()

        # ==========================
    # Search Subject
    # ==========================

    def search_subject(self):

        row = self.controller.search_subject(
            self.subject_id.get()
        )

        if row:

            self.clear_fields()

            self.subject_id.insert(0, row[0])
            self.subject_name.insert(0, row[1])
           
            self.semester.insert(0, row[2])
            self.course_id.insert(0, row[3])

    # ==========================
    # Show All Subjects
    # ==========================

    def show_subjects(self):

        self.tree.delete(*self.tree.get_children())

        rows = self.controller.get_all_subjects()

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

            self.subject_id.insert(0, values[0])
            self.subject_name.insert(0, values[1])
            
            self.semester.insert(0, values[2])
            self.course_id.insert(0, values[3])

    # ==========================
    # Clear Fields
    # ==========================

    def clear_fields(self):

        self.subject_id.delete(0, tk.END)
        self.subject_name.delete(0, tk.END)
        
        self.semester.delete(0, tk.END)
        self.course_id.delete(0, tk.END)