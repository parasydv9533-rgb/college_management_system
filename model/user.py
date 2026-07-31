
class User:

    def __init__(
        self,
        user_id=None,
        full_name="",
        username="",
        password="",
        role=""
    ):

        self.user_id = user_id
        self.full_name = full_name
        self.username = username
        self.password = password
        self.role = role

    def to_tuple(self):
        return (
            self.full_name,
            self.username,
            self.password,
            self.role
        )

    def __str__(self):
        return (
            f"User("
            f"{self.user_id}, "
            f"{self.full_name}, "
            f"{self.username}, "
            f"{self.role})"
        )
