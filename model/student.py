class Student:

    def __init__(
        self,
        student_id=None,
        first_name="",
        last_name="",
        gender="",
        dob="",
        phone="",
        email="",
        address="",
        department_id=None
    ):

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.phone = phone
        self.email = email
        self.address = address
        self.department_id = department_id

    def to_tuple(self):
        return (
            self.first_name,
            self.last_name,
            self.gender,
            self.dob,
            self.phone,
            self.email,
            self.address,
            self.department_id
        )

    def __str__(self):
        return (
            f"Student("
            f"{self.student_id}, "
            f"{self.first_name}, "
            f"{self.last_name}, "
            f"{self.gender}, "
            f"{self.dob}, "
            f"{self.phone}, "
            f"{self.email}, "
            f"{self.address}, "
            f"{self.department_id})"
        )
