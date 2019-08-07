import unittest
from math import MathFunctions


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(MathFunctions.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(MathFunctions.subtract(4, 3), 1)

    def test_mult(self):
        self.assertEqual(MathFunctions.multiply(3, 4), 1)

    def test_div(self):
        self.assertEqual(MathFunctions.divide(6, 2), 3)


if __name__ == '__main__':
    unittest.main()
