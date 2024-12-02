import unittest

from src.PrimosApp import Primos

class TestPrimosApp(unittest.TestCase):
    def test_primo(self):
        assert Primos(7) == True
        assert Primos(13) == True

    def test_no_primo(self):
        assert Primos(4) == False
        assert Primos(9) == False

    def test_numeros_pequenos(self):
        assert Primos(1) == False
        assert Primos(0) == False
        assert Primos(-5) == False
