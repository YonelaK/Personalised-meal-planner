# test_singleton.py

import unittest
from creational_patterns.singleton import DatabaseConnection

class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        conn1 = DatabaseConnection()
        conn2 = DatabaseConnection()
        self.assertIs(conn1, conn2)
        self.assertEqual(conn1.get_connection(), "Connected")

if __name__ == "__main__":
    unittest.main()
