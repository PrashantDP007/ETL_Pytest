import sqlite3
import configparser


class Database:

    def __init__(self):

        config = configparser.ConfigParser()
        config.read("config/config.ini")

        self.source_db = config["DATABASE"]["source_db"]
        self.target_db = config["DATABASE"]["target_db"]

    def get_connection(self, database):
        return sqlite3.connect(database)

    def execute_query(self, database, query, params=None):

        connection = self.get_connection(database)

        try:
            cursor = connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            result = cursor.fetchall()

            return result

        finally:
            connection.close()

    def execute_single_value(self, database, query):

        connection = self.get_connection(database)

        try:
            cursor = connection.cursor()

            cursor.execute(query)

            result = cursor.fetchone()

            return result[0]

        finally:
            connection.close()