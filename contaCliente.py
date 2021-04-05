from datetime import datetime
import datetime


class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    def get_cliente(self, obj):
        return obj.__dict__
    def get_titular_nome(self):
        return self.titular.nome
    def get_titular_sobrenome(self):
        return self.titular.sobrenome
    def get_titular_cpf(self):
        return self.titular.cpf
    def set_titular(self, nome):
         self.titular = nome
    def get_saldo(self):
        return self.saldo
    def get_numero(self):
        return self.numero
    def get_limite(self):
        return self.limite
    def deposita(self, valor):
        self.saldo += valor
        dia_hora = datetime.datetime.today()
        self.historico.transacoes.append('Depósito de {} em {}'.format(valor, dia_hora))
    def saca(self ,valor):
        if self.saldo + self.limite < valor:
            print('Saldo insuficiente')
            return False
        else:
            self.saldo -= valor
            print('Saque realizado.')
            dia_hora = datetime.datetime.today()
            self.historico.transacoes.append('Saque de {} em {}'.format(valor, dia_hora))
            return True
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            print('Transferência não realizada')
            return False
        else:
            destino.deposita(valor)
            dia_hora = datetime.datetime.today()
            print('Transferência realizada com sucesso')
            self.historico.transacoes.append('Transferência de {} para conta {} em {}'.format(valor, destino.numero, dia_hora))
            return True
    def extrato(self):
        print("Extrato: \nNome: {}, Sobrenome: {}, CPF: {}".format(self.titular.nome, self.titular.sobrenome, self.titular.cpf))
        print('Número {}, Saldo {}'.format(self.numero, self.saldo))
        self.historico.transacoes.append('Tirou extrato 1 em {}'.format(datetime.datetime.today()))
    def dados_titular(self):
        return self.titular.__dict__

class Cliente(object):
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_sobrenome(self):
        return self.sobrenome
    def get_cpf(self):
        return self.cpf
    def nome_completo(self):
        nc = f'{self.nome} {self.sobrenome}'
        return nc

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def get_data_abertura(self):
        return self.data_abertura
    def imprime(self):
        print('Transações: ')
        for t in self.transacoes:
            print('-', t)


#main
cliente2 = Cliente('Raquel', 'Guimarães', '21423435')
conta2 = Conta('432-1', cliente2, 300.0, 1000.0)
cliente1 = Cliente('Wendel', 'Freitas', '147852369')
conta1 = Conta('123-4', cliente1, 120.0, 1000.0)


#conta1.saca(250)
#conta1.historico.imprime()
conta2.transfere_para(conta1, 200)
conta2.extrato()
conta2.historico.imprime()
conta1.extrato()
conta1.historico.imprime()


#cliente1.set_nome('Ezequiel')
#print(cliente1.__dict__)

#print('Extrato:', conta1.extrato())

#print('Dados', conta1.dados_titular())

#print('Nome:', conta1.get_titular_nome())
#print('Sobrenome:', conta1.get_titular_sobrenome())
#print('CPF:', conta1.get_titular_cpf())

#print(cliente1.get_nome())
#print(cliente1.get_sobrenome())
#print(cliente1.get_cpf())
#print(cliente1.nome_completo())

#print(conta1.get_cliente(cliente1))

#print('Numero:', conta1.get_numero())
#conta1.set_titular('Ana')
#print('Nome:', conta1.get_titular())
#conta1.deposita(200)
#print('Saldo:', conta1.get_saldo())
#print('Limite:', conta1.get_limite())
#conta1.saca(100)
#print('Saldo:', conta1.get_saldo())
#print('Limite:', conta1.get_limite())
#conta1.transfere_para(conta2, 300)
#print('Nome:', conta2.get_titular())
#print('Numero:', conta2.get_numero())
#print('Saldo:', conta2.get_saldo())
#print('Limite:', conta2.get_limite())
#conta1.extrato()
#conta2.extrato()

