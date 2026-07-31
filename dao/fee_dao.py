
from dao.database import Database
from model.fee import Fee


class FeeDAO:

    # ==========================
    # Save Fee
    # ==========================

    def save(self, fee):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO fees
        (
            student_id,
            total_fee,
            paid_fee,
            remaining_fee,
            payment_date,
            status
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, fee.to_tuple())

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Update Fee
    # ==========================

    def update(self, fee):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE fees
        SET
            student_id=%s,
            total_fee=%s,
            paid_fee=%s,
            remaining_fee=%s,
            payment_date=%s,
            status=%s
        WHERE fee_id=%s
        """

        data = (
            fee.student_id,
            fee.total_fee,
            fee.paid_fee,
            fee.remaining_fee,
            fee.payment_date,
            fee.status,
            fee.fee_id
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Delete Fee
    # ==========================

    def delete(self, fee_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM fees WHERE fee_id=%s"

        cursor.execute(query, (fee_id,))

        conn.commit()

        cursor.close()
        conn.close()

    # ==========================
    # Search Fee
    # ==========================

    def search(self, fee_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM fees WHERE fee_id=%s"

        cursor.execute(query, (fee_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # ==========================
    # Show All Fees
    # ==========================

    def get_all(self):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM fees"

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows
