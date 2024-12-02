import unittest
from src.RectanguloApp import Rectangulo

class TestRectanguloApp(unittest.TestCase):

    def test_area(self):
        rect = Rectangulo(5,3)
        assert rect.area() == 15

    def test_perimetro(self):
        rect = Rectangulo(5,3)
        assert rect.perimetro() == 16

    def test_valores_negativos(self):
        with self.assertRaises(ValueError):
            Rectangulo(-5,3)

    def test_valores_cero(self):
        with self.assertRaises(ValueError):
            Rectangulo(0,3)

    def test_valores_positivos(self):
        rect = Rectangulo(7,4)
        assert rect.area() == 28
        assert rect.perimetro() == 22
