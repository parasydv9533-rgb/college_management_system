from dao.database import Database
from model.course import Course


class CourseDAO:

    # ==========================
    # Save Course
    # ==========================
    def save(self, course):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO courses
        (course_name, duration, total_fee)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, course.to_tuple())

        conn.commit()
        cursor.close()
        conn.close()

    # ==========================
    # Update Course
    # ==========================
    def update(self, course):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE courses
        SET
            course_name=%s,
            duration=%s,
            total_fee=%s
        WHERE course_id=%s
        """

        data = (
            course.course_name,
            course.duration,
            course.total_fee,
            course.course_id
        )

        cursor.execute(query, data)

        conn.commit()
        cursor.close()
        conn.close()

    # ==========================
    # Delete Course
    # ==========================
    def delete(self, course_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM courses WHERE course_id=%s"

        cursor.execute(query, (course_id,))

        conn.commit()
        cursor.close()
        conn.close()

    # ==========================
    # Search Course
    # ==========================
    def search(self, course_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM courses WHERE course_id=%s"

        cursor.execute(query, (course_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # Show All Courses
    # ==========================
    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM courses"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows