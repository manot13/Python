class Veiculo(object):
    def __init__(self, preco, modelo, km):
        self._preco = preco
        self._modelo = modelo
        self._km = km

    def mostra_dados(self):
        print("\nPreço: R$",  self._preco)
        print("Modelo: ", self._modelo)
        print("Km rodados: ", self._km)

    def atualiza_valor(self):
        soma = int(input("Digite o valor atualizado do veículo: "))
        self._preco += soma
        self._mostrar_dados()

class Carro(Veiculo):
    def __init__(self, preco, modelo, km, qtdportas):
        super().__init__(preco, modelo, km)
        self._qtdportas = qtdportas

    def mostrar_dados(self):
        print("\nPreço: R$", self._preco)
        print("Modelo: ", self._modelo)
        print("Km rodados: ", self._km)
        print("Quantidade de portas: ", self._qtdportas)

class Moto(Veiculo):
    def __init__(self, preco, modelo, km, cilindradas):
        super().__init__(preco, modelo, km)
        self._cilindradas = cilindradas

    def mostrar_dados(self):
        print("\nPreço: R$", self._preco)
        print("Modelo: ", self._modelo)
        print("Km rodados: ", self._km)
        print("Cilindradas ", self._cilindradas)


if __name__ == '__main__':
    preco = input("Digite o preço do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    km = float(input("Digite os quilometros rodados: "))
    v1 = Veiculo(preco, modelo, km)
    v1.mostra_dados()

    preco = input("Digite o preço do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    km = float(input("Digite os quilometros rodados: "))
    qtdportas = input("Digite a quantidade de portas do carro: ")
    c1 = Carro(preco, modelo, km, qtdportas)
    c1.mostrar_dados()

    preco = input("Digite o preço do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    km = float(input("Digite os quilometros rodados: "))
    cilindradas = input("Digite a quantidade de cilindradas da moto: ")
    m1 = Moto(preco, modelo, km, cilindradas)
    m1.mostrar_dados()

    v1.atualiza_valor()
    c1.atualiza_valor()
    m1.atualiza_valor()
    