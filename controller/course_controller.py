from dao.course_dao import CourseDAO
from model.course import Course


class CourseController:

    def __init__(self):
        self.dao = CourseDAO()

    def save_course(self, course_name, duration, total_fee):

        course = Course(
            None,
            course_name,
            duration,
            total_fee
        )

        self.dao.save(course)

    def update_course(
        self,
        course_id,
        course_name,
        duration,
        total_fee
    ):

        course = Course(
            course_id,
            course_name,
            duration,
            total_fee
        )

        self.dao.update(course)

        self.dao.update(course)

    def delete_course(self, course_id):
        self.dao.delete(course_id)

    def search_course(self, course_id):
        return self.dao.search(course_id)

    def get_all_courses(self):
        return self.dao.get_all()