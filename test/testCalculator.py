import unittest
from src.CalculatorApp import suma,resta,multiplicacion, division

class CalculatorTest(unittest.TestCase):
    def test_suma(self):
        assert suma(3,2) == 5

    def test_resta(self):
        assert resta(3,2) == 1

    def test_multiplicacion(self):
        assert multiplicacion(5,5)==25

    def test_division(self):
        result = division(10,2)
        expected = 5
        assert  result == expected
