
class Department:

    def __init__(
        self,
        department_id=None,
        department_name="",
        hod_name=""
    ):

        self.department_id = department_id
        self.department_name = department_name
        self.hod_name = hod_name

    def to_tuple(self):
        return (
            self.department_name,
            self.hod_name
        )

    def __str__(self):
        return (
            f"Department("
            f"{self.department_id}, "
            f"{self.department_name}, "
            f"{self.hod_name})"
        )
