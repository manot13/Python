from abc import ABC, abstractmethod

class FormaGeometrcia(ABC):
    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimetro(self):
        pass
    def mensagem(self):
        print('\nEssa mensagem está sendo puxada de uma super classe abstrata!')
        print(self.__class__.__name__)

class Quadrado(FormaGeometrcia):
    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return self.lado * 4

class Circulo(FormaGeometrcia):
    def __init__(self, raio):
        self.raio = raio
    def get_raio(self):
        return self.raio
    def area(self):
        return 3.14 * pow(self.raio, 2)
    def perimetro(self):
        return 2*3.14*self.raio

quadrado1 = Quadrado(6)
print(quadrado1.perimetro())
print(quadrado1.area())
print()
circulo1 = Circulo(4)
print(circulo1.area())
print(circulo1.perimetro())
circulo1.mensagem()
