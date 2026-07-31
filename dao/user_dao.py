
from dao.database import Database
from model.user import User


class UserDAO:

    # ==========================
    # Save User
    # ==========================

    def save(self, user):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO users
        (
            full_name,
            username,
            password,
            role
        )
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(query, user.to_tuple())

        conn.commit()

        cursor.close()
        conn.close()


      # ==========================
        # Check Username
        # ==========================
    # ==========================
# Check Username
# ==========================

    def check_username(self, username):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM users
        WHERE username=%s
        """

        cursor.execute(query, (username,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # Reset Password
    # ==========================


    def reset_password(self, username, new_password):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE users
        SET password=%s
        WHERE username=%s
        """

        cursor.execute(query, (new_password, username))

        conn.commit()

        result = cursor.rowcount

        cursor.close()
        conn.close()

        return result

    # ==========================
    # Update User
    # ==========================

    def update(self, user):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE users
        SET
            full_name=%s,
            username=%s,
            password=%s,
            role=%s
        WHERE user_id=%s
        """

        data = (
            user.full_name,
            user.username,
            user.password,
            user.role,
            user.user_id
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Delete User
    # ==========================

    def delete(self, user_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE user_id=%s"

        cursor.execute(query, (user_id,))

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Search User
    # ==========================

    def search(self, user_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE user_id=%s"

        cursor.execute(query, (user_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # User Login
    # ==========================

    def login(self, username, password):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM users
        WHERE username=%s
        AND password=%s
        """

        cursor.execute(query, (username, password))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # Show All Users
    # ==========================

    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows
