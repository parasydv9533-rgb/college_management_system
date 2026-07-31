
class Attendance:

    def __init__(
        self,
        attendance_id=None,
        student_id=None,
        attendance_date="",
        status=""
    ):

        self.attendance_id = attendance_id
        self.student_id = student_id
        self.attendance_date = attendance_date
        self.status = status

    def to_tuple(self):

        return (
            self.student_id,
            self.attendance_date,
            self.status
        )

    def __str__(self):

        return (
            f"Attendance("
            f"{self.attendance_id}, "
            f"{self.student_id}, "
            f"{self.attendance_date}, "
            f"{self.status})"
        )
