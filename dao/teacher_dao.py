
from dao.database import Database
from model.teacher import Teacher


class TeacherDAO:

    # ==========================
    # Save Teacher
    # ==========================

    def save(self, teacher):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO teachers
        (
            first_name,
            last_name,
            gender,
            phone,
            email,
            qualification,
            salary,
            department_id
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, teacher.to_tuple())

        conn.commit()
        conn.close()

    # ==========================
    # Update Teacher
    # ==========================

    def update(self, teacher):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE teachers
        SET
            first_name=%s,
            last_name=%s,
            gender=%s,
            phone=%s,
            email=%s,
            qualification=%s,
            salary=%s,
            department_id=%s
        WHERE teacher_id=%s
        """

        data = (
            teacher.first_name,
            teacher.last_name,
            teacher.gender,
            teacher.phone,
            teacher.email,
            teacher.qualification,
            teacher.salary,
            teacher.department_id,
            teacher.teacher_id
        )

        cursor.execute(query, data)

        conn.commit()
        conn.close()

    # ==========================
    # Delete Teacher
    # ==========================

    def delete(self, teacher_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM teachers WHERE teacher_id=%s"

        cursor.execute(query, (teacher_id,))

        conn.commit()
        conn.close()

    # ==========================
    # Search Teacher
    # ==========================

    def search(self, teacher_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM teachers WHERE teacher_id=%s"

        cursor.execute(query, (teacher_id,))

        row = cursor.fetchone()

        conn.close()

        return row

    # ==========================
    # Show All Teachers
    # ==========================

    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM teachers"

        cursor.execute(query)

        rows = cursor.fetchall()

        conn.close()

        return rows
