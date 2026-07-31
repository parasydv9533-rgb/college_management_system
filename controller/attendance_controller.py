
from dao.attendance_dao import AttendanceDAO
from model.attendance import Attendance


class AttendanceController:

    def __init__(self):
        self.dao = AttendanceDAO()

    # ==========================
    # Save Attendance
    # ==========================

    def save_attendance(
        self,
        student_id,
        attendance_date,
        status
    ):

        attendance = Attendance(
            None,
            student_id,
            attendance_date,
            status
        )

        self.dao.save(attendance)

    # ==========================
    # Update Attendance
    # ==========================

    def update_attendance(
        self,
        attendance_id,
        student_id,
        attendance_date,
        status
    ):

        attendance = Attendance(
            attendance_id,
            student_id,
            attendance_date,
            status
        )

        self.dao.update(attendance)

    # ==========================
    # Delete Attendance
    # ==========================

    def delete_attendance(self, attendance_id):

        self.dao.delete(attendance_id)

    # ==========================
    # Search Attendance
    # ==========================

    def search_attendance(self, attendance_id):

        return self.dao.search(attendance_id)

    # ==========================
    # Show All Attendance
    # ==========================

    def get_all_attendance(self):

        return self.dao.get_all()
