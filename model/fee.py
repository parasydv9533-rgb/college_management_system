
class Fee:

    def __init__(
        self,
        fee_id=None,
        student_id=None,
        total_fee=0.0,
        paid_fee=0.0,
        remaining_fee=0.0,
        payment_date="",
        status=""
    ):

        self.fee_id = fee_id
        self.student_id = student_id
        self.total_fee = total_fee
        self.paid_fee = paid_fee
        self.remaining_fee = remaining_fee
        self.payment_date = payment_date
        self.status = status

    def to_tuple(self):

        return (
            self.student_id,
            self.total_fee,
            self.paid_fee,
            self.remaining_fee,
            self.payment_date,
            self.status
        )

    def __str__(self):

        return (
            f"Fee("
            f"{self.fee_id}, "
            f"{self.student_id}, "
            f"{self.total_fee}, "
            f"{self.paid_fee}, "
            f"{self.remaining_fee}, "
            f"{self.payment_date}, "
            f"{self.status})"
        )
