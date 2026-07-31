
import re


class Validation:

    # ==========================
    # Empty Validation
    # ==========================

    @staticmethod
    def is_empty(value):

        if str(value).strip() == "":
            return True

        return False

    # ==========================
    # Phone Validation
    # ==========================

    @staticmethod
    def valid_phone(phone):

        pattern = r"^[6-9][0-9]{9}$"

        return re.match(pattern, phone)

    # ==========================
    # Email Validation
    # ==========================

    @staticmethod
    def valid_email(email):

        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.match(pattern, email)

    # ==========================
    # Number Validation
    # ==========================

    @staticmethod
    def is_number(value):

        try:

            float(value)

            return True

        except:

            return False

    # ==========================
    # Positive Number
    # ==========================

    @staticmethod
    def is_positive(value):

        try:

            return float(value) >= 0

        except:

            return False

    # ==========================
    # Date Validation
    # YYYY-MM-DD
    # ==========================

    @staticmethod
    def valid_date(date):

        pattern = r"^\d{4}-\d{2}-\d{2}$"

        return re.match(pattern, date)
