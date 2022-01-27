import unittest

from src.calculator import add, subtract


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, add(2, 2))

    def test_add(self):
        self.assertEqual(4, subtract(3, 5))


if __name__ == '__main__':
    unittest.main()
