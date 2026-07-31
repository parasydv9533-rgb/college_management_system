
class Teacher:

    def __init__(
        self,
        teacher_id=None,
        first_name="",
        last_name="",
        gender="",
        phone="",
        email="",
        qualification="",
        salary=0.0,
        department_id=None
    ):

        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.email = email
        self.qualification = qualification
        self.salary = salary
        self.department_id = department_id

    def to_tuple(self):
        return (
            self.first_name,
            self.last_name,
            self.gender,
            self.phone,
            self.email,
            self.qualification,
            self.salary,
            self.department_id
        )

    def __str__(self):
        return (
            f"Teacher("
            f"{self.teacher_id}, "
            f"{self.first_name}, "
            f"{self.last_name}, "
            f"{self.gender}, "
            f"{self.phone}, "
            f"{self.email}, "
            f"{self.qualification}, "
            f"{self.salary}, "
            f"{self.department_id})"
        )
