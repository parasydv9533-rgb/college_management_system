
from dao.database import Database
from model.subject import Subject


class SubjectDAO:

    # ==========================
    # Save Subject
    # ==========================

    def save(self, subject):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO subjects
        (
            subject_name,
            
            semester,
            course_id
        )
        VALUES (%s,%s,%s)
        """

        cursor.execute(query, subject.to_tuple())

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Update Subject
    # ==========================

    def update(self, subject):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE subjects
        SET
            subject_name=%s,
            
            semester=%s,
            course_id=%s
        WHERE subject_id=%s
        """

        data = (
            subject.subject_name,
            subject.semester,
            subject.course_id,
            subject.subject_id
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Delete Subject
    # ==========================

    def delete(self, subject_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM subjects WHERE subject_id=%s"

        cursor.execute(query, (subject_id,))

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Search Subject
    # ==========================

    def search(self, subject_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM subjects WHERE subject_id=%s"

        cursor.execute(query, (subject_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # Show All Subjects
    # ==========================

    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM subjects"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows
