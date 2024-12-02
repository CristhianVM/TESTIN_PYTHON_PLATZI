class Rectangulo:

    def __init__(self, largo:int=0, ancho:int=0):
        if largo <= 0 or ancho <= 0:
            raise ValueError({"message": "El largo y ancho deben ser positivos"})
        self.largo = largo
        self.ancho = ancho

    def area(self)-> int:
        return self.largo * self.ancho

    def perimetro(self)-> int:
        return 2 * (self.largo + self.ancho)