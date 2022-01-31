import unittest

from src.calculator import add, subtract, multiply


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, add(2, 2))

    def test_subtract(self):
        self.assertEqual(2, subtract(9, 5))

    def test_subtract(self):
        self.assertEqual(12, multiply(4, 3))

if __name__ == '__main__':
    unittest.main()
