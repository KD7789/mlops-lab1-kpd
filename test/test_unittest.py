import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    
    def test_fun4_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator.fun4(1, 2, "3")
        with self.assertRaises(ValueError):
            calculator.fun4(1, None, 3)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 4), 2.5)
        self.assertEqual(calculator.divide(-6, 3), -2)
        self.assertEqual(calculator.divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_divide_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator.divide("a", 2)
        with self.assertRaises(ValueError):
            calculator.divide(True, 2)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)
        self.assertEqual(calculator.power(2, -1), 0.5)
        self.assertEqual(calculator.power(4, 0.5), 2.0)

    def test_power_negative_base_fractional_exponent(self):
        with self.assertRaises(ValueError):
            calculator.power(-4, 0.5)

    def test_average(self):
        self.assertEqual(calculator.average(1, 2, 3), 2.0)
        self.assertEqual(calculator.average(5), 5.0)
        self.assertEqual(calculator.average(-1, 1), 0.0)

    def test_average_no_input(self):
        with self.assertRaises(ValueError):
            calculator.average()

    def test_modulo(self):
        self.assertEqual(calculator.modulo(10, 3), 1)
        self.assertEqual(calculator.modulo(9, 3), 0)
        self.assertEqual(calculator.modulo(-7, 3), 2)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.modulo(5, 0)

    def test_sqrt(self):
        self.assertEqual(calculator.sqrt(16), 4.0)
        self.assertEqual(calculator.sqrt(0), 0.0)
        self.assertAlmostEqual(calculator.sqrt(2), 1.41421356, places=6)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            calculator.sqrt(-1)

    def test_sqrt_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator.sqrt("16")    


if __name__ == '__main__':
    unittest.main()