import unittest
from functions_to_test import Calculator


class FunctionTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(4, 5), 9)
        self.assertNotEqual(Calculator.add(3, 4), 4)
        self.assertEqual(Calculator.add(10, 15), 25)
        self.assertEqual(Calculator.add(100, 150), 250)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 1), 4)
        self.assertEqual(Calculator.subtract(15, 3), 12)
        self.assertEqual(Calculator.subtract(150, 250), -100)

    def test_multiple(self):
        self.assertEqual(Calculator.multiply(5, 2), 10)
        self.assertEqual(Calculator.multiply(25, 4), 100)

    def test_divide(self):
        try:
            Calculator.divide(20, 0)
        except ZeroDivisionError:
            self.assertEqual(0, 0)
        self.assertEqual(Calculator.divide(20, 10), 2)
        self.assertEqual(Calculator.divide(100, 2), 50)
        self.assertNotEqual(Calculator.divide(5000, 250), 6)
