
from dao.teacher_dao import TeacherDAO
from model.teacher import Teacher


class TeacherController:

    def __init__(self):
        self.dao = TeacherDAO()

    # ==========================
    # Save Teacher
    # ==========================

    def save_teacher(
        self,
        first_name,
        last_name,
        gender,
        phone,
        email,
        qualification,
        salary,
        department_id
    ):

        teacher = Teacher(
            None,
            first_name,
            last_name,
            gender,
            phone,
            email,
            qualification,
            salary,
            department_id
        )

        self.dao.save(teacher)

    # ==========================
    # Update Teacher
    # ==========================

    def update_teacher(
        self,
        teacher_id,
        first_name,
        last_name,
        gender,
        phone,
        email,
        qualification,
        salary,
        department_id
    ):

        teacher = Teacher(
            teacher_id,
            first_name,
            last_name,
            gender,
            phone,
            email,
            qualification,
            salary,
            department_id
        )

        self.dao.update(teacher)

    # ==========================
    # Delete Teacher
    # ==========================

    def delete_teacher(self, teacher_id):

        self.dao.delete(teacher_id)

    # ==========================
    # Search Teacher
    # ==========================

    def search_teacher(self, teacher_id):

        return self.dao.search(teacher_id)

    # ==========================
    # Show All Teachers
    # ==========================

    def get_all_teachers(self):

        return self.dao.get_all()
