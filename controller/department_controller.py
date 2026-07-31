
from dao.department_dao import DepartmentDAO
from model.department import Department


class DepartmentController:

    def __init__(self):
        self.dao = DepartmentDAO()

    # ==========================
    # Save Department
    # ==========================

    def save_department(
        self,
        department_name,
        hod_name
    ):

        department = Department(
            None,
            department_name,
            hod_name
        )

        self.dao.save(department)

    # ==========================
    # Update Department
    # ==========================

    def update_department(
        self,
        department_id,
        department_name,
        hod_name
    ):

        department = Department(
            department_id,
            department_name,
            hod_name
        )

        self.dao.update(department)

    # ==========================
    # Delete Department
    # ==========================

    def delete_department(self, department_id):

        self.dao.delete(department_id)

    # ==========================
    # Search Department
    # ==========================

    def search_department(self, department_id):

        return self.dao.search(department_id)

    # ==========================
    # Show All Departments
    # ==========================

    def get_all_departments(self):

        return self.dao.get_all()
