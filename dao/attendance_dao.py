
from dao.database import Database
from model.attendance import Attendance


class AttendanceDAO:

    # ==========================
    # Save Attendance
    # ==========================

    def save(self, attendance):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO attendance
        (
            student_id,
            attendance_date,
            status
        )
        VALUES (%s,%s,%s)
        """

        cursor.execute(query, attendance.to_tuple())

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Update Attendance
    # ==========================

    def update(self, attendance):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE attendance
        SET
            student_id=%s,
            attendance_date=%s,
            status=%s
        WHERE attendance_id=%s
        """

        data = (
            attendance.student_id,
            attendance.attendance_date,
            attendance.status,
            attendance.attendance_id
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Delete Attendance
    # ==========================

    def delete(self, attendance_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM attendance WHERE attendance_id=%s"

        cursor.execute(query, (attendance_id,))

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Search Attendance
    # ==========================

    def search(self, attendance_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM attendance WHERE attendance_id=%s"

        cursor.execute(query, (attendance_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # Show All Attendance
    # ==========================

    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM attendance"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows
