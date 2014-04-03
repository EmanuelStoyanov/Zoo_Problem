import database_ops
import unittest


class DatabaseTests(unittest.TestCase):
    # Connect to database
    conn = sqlite3.connect('animals.db')
    c = conn.cursor()
    def setUp(self):



    def test_get_animal(self):

    def tearDown(self):
