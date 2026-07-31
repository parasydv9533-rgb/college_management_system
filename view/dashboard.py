
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from view.student_view import StudentView
from view.teacher_view import TeacherView
from view.course_view import CourseView
from view.department_view import DepartmentView
from view.subject_view import SubjectView
from view.user_view import UserView
from view.fee_view import FeeView
from view.attendance_view import AttendanceView


class Dashboard:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("College Management System")
        self.root.geometry("1100x650")
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(True,True)

        self.create_widgets()

    def create_widgets(self):

        # ==========================
        # Header
        # ==========================

        header = tk.Frame(
            self.root,
            bg="#2c3e50",
            height=80
        )

        header.pack(fill="x")

        tk.Label(
            header,
            text="COLLEGE MANAGEMENT SYSTEM",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

        tk.Label(
            header,
            text=datetime.now().strftime("%d-%m-%Y   %I:%M:%S %p"),
            bg="#2c3e50",
            fg="white",
            font=("Arial", 10)
        ).pack()

        # ==========================
        # Body
        # ==========================

        body = tk.Frame(
            self.root,
            bg="#ecf0f1"
        )

        body.pack(pady=30)

        

        buttons = [

            # Row 1
            ("Department", "#d35400", self.open_department),
            ("Course", "#8e44ad", self.open_course),
            ("Subject", "#16a085", self.open_subject),

            # Row 2
            ("Student", "#27ae60", self.open_student),
            ("Teacher", "#2980b9", self.open_teacher),
            ("Users", "#7f8c8d", self.open_user),

            # Row 3
            ("Attendance", "#c0392b", self.open_attendance),
            ("Fee", "#f39c12", self.open_fee)



        ]

        row = 0
        col = 0

        for text, color, command in buttons:

            tk.Button(
                body,
                text=text,
                width=20,
                height=2,
                bg=color,
                fg="white",
                font=("Arial", 12, "bold"),
                cursor="hand2",
                command=command
            ).grid(
                row=row,
                column=col,
                padx=20,
                pady=20
            )

            col += 1

            if col == 3:
                col = 0
                row += 1

        # ==========================
        # Logout
        # ==========================

        tk.Button(
            self.root,
            text="Logout",
            bg="red",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20,
            cursor="hand2",
            command=self.logout
        ).pack(pady=20)

    # ==========================
    # Open Forms
    # ==========================

    def open_student(self):
        StudentView()

    def open_teacher(self):
        TeacherView()

    def open_course(self):
        CourseView()

    def open_department(self):
        DepartmentView()

    def open_subject(self):
        SubjectView()

    def open_user(self):
        UserView()

    def open_fee(self):
        FeeView()

    def open_attendance(self):
        AttendanceView()

    # ==========================
    # Logout
    # ==========================

    def logout(self):

        if messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        ):

            self.root.destroy()

            from view.login import Login
            Login()
