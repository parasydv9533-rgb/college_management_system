
class Enrollment:

    def __init__(
        self,
        enrollment_id,
        student_id,
        course_id,
        enrollment_date
    ):

        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def to_tuple(self):

        return (
            self.student_id,
            self.course_id,
            self.enrollment_date
        )
