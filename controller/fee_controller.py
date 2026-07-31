
from dao.fee_dao import FeeDAO
from model.fee import Fee


class FeeController:

    def __init__(self):
        self.dao = FeeDAO()

    # ==========================
    # Save Fee
    # ==========================

    def save_fee(
        self,
        student_id,
        total_fee,
        paid_fee,
        remaining_fee,
        payment_date,
        status
    ):

        fee = Fee(
            None,
            student_id,
            total_fee,
            paid_fee,
            remaining_fee,
            payment_date,
            status
        )

        self.dao.save(fee)

    # ==========================
    # Update Fee
    # ==========================

    def update_fee(
        self,
        fee_id,
        student_id,
        total_fee,
        paid_fee,
        remaining_fee,
        payment_date,
        status
    ):

        fee = Fee(
            fee_id,
            student_id,
            total_fee,
            paid_fee,
            remaining_fee,
            payment_date,
            status
        )

        self.dao.update(fee)

    # ==========================
    # Delete Fee
    # ==========================

    def delete_fee(self, fee_id):

        self.dao.delete(fee_id)

    # ==========================
    # Search Fee
    # ==========================

    def search_fee(self, fee_id):

        return self.dao.search(fee_id)

    # ==========================
    # Show All Fees
    # ==========================

    def get_all_fees(self):

        return self.dao.get_all()
