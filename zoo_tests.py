import unittest
import zoo


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.m = zoo.Zoo(15, 1000)

    def test_initials(self):
        self.assertEqual(15, self.m.capacity)


if __name__ == '__main__':
    unittest.main()
   