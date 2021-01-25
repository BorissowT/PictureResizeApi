import unittest

from api_container.db.database import connect_api_to_db


class ApiDBTest(unittest.TestCase):

    def test_if_db_initialized(self):
        try:
            connect_api_to_db()
        except Exception:
            self.fail("ERROR")

