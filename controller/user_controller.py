
from dao.user_dao import UserDAO
from model.user import User


class UserController:

    def __init__(self):
        self.dao = UserDAO()

    # ==========================
    # Save User
    # ==========================

    def save_user(
        self,
        
        username,
        password,
        role
    ):

        user = User(
            None,
        
            username,
            password,
            role
        )

        self.dao.save(user)

    # ==========================
    # Update User
    # ==========================

    def update_user(
        self,
        user_id,
        full_name,
        username,
        password,
        role
    ):

        user = User(
            user_id,
            full_name,
            username,
            password,
            role
        )

        self.dao.update(user)

    # ==========================
    # Delete User
    # ==========================

    def delete_user(self, user_id):

        self.dao.delete(user_id)

    # ==========================
    # Search User
    # ==========================

    def search_user(self, user_id):

        return self.dao.search(user_id)

    # ==========================
    # Login
    # ==========================

    def login(self, username, password):

        return self.dao.login(username, password)

    def reset_password(self, username, new_password):
        return self.dao.reset_password(username, new_password)

    # ==========================
    # Show All Users
    # ==========================

    def get_all_users(self):

        return self.dao.get_all()

    # ==========================
    # Check Username
    # ==========================

    def check_username(self, username):

        return self.dao.check_username(username)
