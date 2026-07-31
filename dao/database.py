import mysql.connector


class Database:

    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Paras@2006",
            database="college_db3"
        )

   