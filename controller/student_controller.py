
from dao.student_dao import StudentDAO
from model.student import Student


class StudentController:

    def __init__(self):
        self.dao = StudentDAO()

    # ==========================
    # Save Student
    # ==========================
    def save_student(
        self,
        first_name,
        last_name,
        gender,
        dob,
        phone,
        email,
        address,
        department_id
    ):

        student = Student(
            None,
            first_name,
            last_name,
            gender,
            dob,
            phone,
            email,
            address,
            department_id
        )

        self.dao.save(student)

    # ==========================
    # Update Student
    # ==========================
    def update_student(
        self,
        student_id,
        first_name,
        last_name,
        gender,
        dob,
        phone,
        email,
        address,
        department_id
    ):

        student = Student(
            student_id,
            first_name,
            last_name,
            gender,
            dob,
            phone,
            email,
            address,
            department_id
        )

        self.dao.update(student)

    # ==========================
    # Delete Student
    # ==========================
    def delete_student(self, student_id):

        self.dao.delete(student_id)

    # ==========================
    # Search Student
    # ==========================
    def search_student(self, student_id):

        return self.dao.search(student_id)

    # ==========================
    # Show All Students
    # ==========================
    def get_all_students(self):

        return self.dao.get_all()
