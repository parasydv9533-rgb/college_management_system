
from dao.subject_dao import SubjectDAO
from model.subject import Subject


class SubjectController:

    def __init__(self):
        self.dao = SubjectDAO()

    # ==========================
    # Save Subject
    # ==========================

    def save_subject(
        self,
        subject_name,
        
        semester,
        course_id
    ):

        subject = Subject(
            None,
            subject_name,
        
            semester,
            course_id
        )

        self.dao.save(subject)

    # ==========================
    # Update Subject
    # ==========================

    def update_subject(
        self,
        subject_id,
        subject_name,
        semester,
        course_id
    ):

        subject = Subject(
            subject_id,
            subject_name,
            semester,
            course_id
        )

        self.dao.update(subject)

    # ==========================
    # Delete Subject
    # ==========================

    def delete_subject(self, subject_id):

        self.dao.delete(subject_id)

    # ==========================
    # Search Subject
    # ==========================

    def search_subject(self, subject_id):

        return self.dao.search(subject_id)

    # ==========================
    # Show All Subjects
    # ==========================

    def get_all_subjects(self):

        return self.dao.get_all()
