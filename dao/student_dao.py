
from dao.database import Database
from model.student import Student


class StudentDAO:

    # ==========================
    # Save Student
    # ==========================
    def save(self, student):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO students
        (first_name,last_name,gender,dob,phone,email,address,department_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, student.to_tuple())

        conn.commit()
        conn.close()

    # ==========================
    # Update Student
    # ==========================
    def update(self, student):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE students
        SET first_name=%s,
            last_name=%s,
            gender=%s,
            dob=%s,
            phone=%s,
            email=%s,
            address=%s,
            department_id=%s
        WHERE student_id=%s
        """

        data = (
            student.first_name,
            student.last_name,
            student.gender,
            student.dob,
            student.phone,
            student.email,
            student.address,
            student.department_id,
            student.student_id
        )

        cursor.execute(query, data)

        conn.commit()
        conn.close()

    # ==========================
    # Delete Student
    # ==========================
    def delete(self, student_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM students WHERE student_id=%s"

        cursor.execute(query, (student_id,))

        conn.commit()
        conn.close()

    # ==========================
    # Search Student
    # ==========================
    def search(self, student_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM students WHERE student_id=%s"

        cursor.execute(query, (student_id,))

        row = cursor.fetchone()

        conn.close()

        return row

    # ==========================
    # Show All Students
    # ==========================
    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM students"

        cursor.execute(query)

        rows = cursor.fetchall()

        conn.close()

        return rows
