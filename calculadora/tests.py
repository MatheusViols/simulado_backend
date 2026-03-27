from django.test import TestCase

from .calculator import Calculator


class CalculatorTestCase(TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(10, 20), -10)
        self.assertEqual(calc.subtract(5, 2), 3)
        self.assertEqual(calc.subtract(10, -10), 20)


    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(10, 20), 200)
        self.assertEqual(calc.multiply(-10, 20), -200)
        self.assertEqual(calc.multiply(-10, -20), 200)
        self.assertEqual(calc.multiply(0, 10), 0)


    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(20, 4), 5)
        self.assertEqual(calc.divide(-10, 2), -5)
        self.assertEqual(calc.divide(-10, -2), 5)

        self.assertEqual(calc.divide(10, 0), ZeroDivisionError)
        self.assertEqual(calc.divide(0, 10), ZeroDivisionError)

    # TODO(aluno): adicionar testes para subtract, multiply e divide.
