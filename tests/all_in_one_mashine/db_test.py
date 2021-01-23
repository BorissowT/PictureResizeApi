import unittest
import mysql.connector
import os


class DbTest(unittest.TestCase):

    db_user = os.environ.get("DB_MYSQL_USER")
    db_pass = os.environ.get("DB_MYSQL_PASS")
    db_address = os.environ.get("DB_MYSQL_ADDRESS")
    db_host_name = db_address.split(":")[0]
    db_host_port = db_address.split(":")[1]

    def set_connection(self):
        connection = mysql.connector.connect(
            host=self.db_host_name,
            user=self.db_user,
            password=self.db_pass,
            port=self.db_host_port
        )

    def test_connection(self):
        self.assertRaises(mysql.connector.errors.ProgrammingError, self.set_connection())