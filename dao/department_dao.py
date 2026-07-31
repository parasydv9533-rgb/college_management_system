
from dao.database import Database
from model.department import Department


class DepartmentDAO:

    # ==========================
    # Save Department
    # ==========================

    def save(self, department):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO departments
        (
            department_name,
            hod_name
        )
        VALUES (%s,%s)
        """

        cursor.execute(query, department.to_tuple())

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Update Department
    # ==========================

    def update(self, department):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE departments
        SET
            department_name=%s,
            hod_name=%s
        WHERE department_id=%s
        """

        data = (
            department.department_name,
            department.hod_name,
            department.department_id
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Delete Department
    # ==========================

    def delete(self, department_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM departments WHERE department_id=%s"

        cursor.execute(query, (department_id,))

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Search Department
    # ==========================

    def search(self, department_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM departments WHERE department_id=%s"

        cursor.execute(query, (department_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # Show All Departments
    # ==========================

    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM departments"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows
