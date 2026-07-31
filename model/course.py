class Course:

    def __init__(
        self,
        course_id=None,
        course_name="",
        duration="",
        total_fee=0
    ):

        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration
        self.total_fee = total_fee

    def to_tuple(self):
        return (
            self.course_name,
            self.duration,
            self.total_fee
        )