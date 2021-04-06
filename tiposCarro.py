from abc import ABC, abstractmethod

class Carro(ABC):
    nome = None
    preco_base = None

    def get_nome(self):
        return self.nome
    def get_preco_base(self):
        return self.preco_base
    @abstractmethod
    def retorna_preco_diaria(self):
        pass
class Economico(Carro):
    def __init__(self, nome, preco_base):
        Carro.nome = nome
        Carro.preco_base = preco_base
    def retorna_preco_diaria(self):
        return self.get_preco_base()

class Intermediario(Carro):
    def __init__(self, nome, preco_base):
        Carro.nome = nome
        Carro.preco_base = preco_base
    def retorna_preco_diaria(self):
        return self.get_preco_base() * 0.1

o_eco = Economico('Uno', 1000.00)
print(f'Nome: {o_eco.get_nome()}')
print(f'Diaria: {o_eco.retorna_preco_diaria()}')

o_int = Intermediario('HB20', 100.00)
print(f'Nome: {o_int.get_nome()}')
print(f'Diaria: {o_int.retorna_preco_diaria()}')