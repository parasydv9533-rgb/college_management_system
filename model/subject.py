
class Subject:

    def __init__(
        self,
        subject_id=None,
        subject_name="",
        semester="",
        course_id=None
    ):

        self.subject_id = subject_id
        self.subject_name = subject_name
        self.semester = semester
        self.course_id = course_id

    def to_tuple(self):
        return (
            self.subject_name,
            self.semester,
            self.course_id
        )

    def __str__(self):
        return (
            f"Subject("
            f"{self.subject_id}, "
            f"{self.subject_name}, "
            f"{self.subject_code}, "
            f"{self.semester}, "
            f"{self.course_id})"
        )
