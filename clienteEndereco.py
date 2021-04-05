class Cliente(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def insere_endereco(self, cidade, estado):
        obj_endereco = Endereco(cidade, estado)
        self.enderecos.append(obj_endereco)
    def mostra_endereco(self):
        print('Endereços do cliente: ')
        for obj_endereco in self.enderecos:
            print(obj_endereco.get_cidade(), obj_endereco.get_estado())
    def insere_endereco2(self, obj_endereco):
        self.enderecos.append(obj_endereco)
    def mostra_endereco2(self):
        print(f'\nEndereços do cliente {self.nome}')
        if self.enderecos == []:
            print('O cliente não possui endereço cadastrado.')
        else:
            for obj_endereco in self.enderecos:
                print(obj_endereco.get_cidade(), obj_endereco.get_estado())
    def remover_endereco(self, obj_endereco):
        self.enderecos.remove(obj_endereco)


class Endereco(object):
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    def get_cidade(self):
        return self.cidade
    def get_estado(self):
        return self.estado

if __name__ == '__main__':

    cliente1 = Cliente('Italo', 90)

    print('\nNome: ', cliente1.get_nome())
    print('Idade: ', cliente1.get_idade())

    cliente1.insere_endereco('Belo Horizonte', 'MG\n')
    cliente1.mostra_endereco()

    cliente2 = Cliente('Erick', 27)
    cliente2.mostra_endereco2()
    cliente2.insere_endereco('Brasília', 'DF')
    cliente2.insere_endereco('Bahia', 'BA')

    print('\nNome: ', cliente2.get_nome())
    print('Idade: ', cliente2.get_idade())
    #cliente2.mostra_endereco()
    endereco2 = Endereco('Amazonas', 'AM')
    cliente2.insere_endereco2(endereco2)
    cliente2.mostra_endereco2()
    cliente2.remover_endereco(endereco2)
    cliente2.mostra_endereco2()
