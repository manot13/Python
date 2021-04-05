from datetime import datetime
import datetime
class Cliente(object):
    def __init__(self, identidade, nome):
       self.identidade = identidade
       self.nome = nome
    def get_identidade(self):
        return self.identidade
    def get_nome(self):
        return self.nome

class CarrinhoCompra(object):
    def __init__(self, numero_pedido, cliente):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.produtos = []
    def get_num_pedido(self):
        return self.numero_pedido
    def get_cliente_nome(self):
        return self.cliente.get_nome()
    def mostra_carrinho(self):
        print('\nSeu carrinho contém: ')
        for produto in self.produtos:
            print('\nIdt:', produto.get_nome_produto())
            print('Descrição:', produto.get_descricao())
            print('Preço:', produto.get_preco())
            print('Quantidade:', produto.get_qtd())
    def mostra_carrinho2(self):
        qtd = len(self.produtos)
        if qtd == 0:
            print('Carrinho vazio')
        else:
            print('\nMostra carrinho 2:')
            for produto in self.produtos:
                print(produto)
            print('Quantidade de itens:', qtd)
    def insere_produto(self, produto):
        self.produtos.append(produto)
    def retorna_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.get_preco() * produto.get_qtd()
        return total
    def remove_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
        else:
            print('Este produto não existe no carrinho!')
    def remove_produto2(self):
        if not self.produtos:
            print('Carrinhos vazio!')
        else:
            print('\n')
            for produtos in self.produtos:
                print(' Produtos no carrinho: ', produtos)
            opcao = int(input(' \n Escolha o produto que deseja remover pela ordem de amostragem: '))
            self.produtos.pop(opcao-1)
    def fecha_carrinho(self):
        print('\n')
        for produtos in self.produtos:
            print(' Produtos adquiridos: ', produtos)
        print('\n Sua compra foi finalizada!\n Valor total da compra: R$ ', self.retorna_total())
    def fecha_carrinho2(self):
        dia_hora = datetime.datetime.today()
        print('\n')
        print(' Pedido:', self.get_num_pedido())
        print(' Nome:', self.cliente.get_nome())
        print(' Data:', dia_hora)
        for produtos in self.produtos:
            print(' Produtos adquiridos: ', produtos)
        print('\n Sua compra foi finalizada!\n Valor total da compra: R$', self.retorna_total())
    def altera_qtd(self, produto, nova_qtd):
        if produto in self.produtos:
            produto.set_qtd(nova_qtd)
    def altera_qtd2(self):
        if not self.produtos:
            print('Carrinho vazio!')
        else:
            self.mostra_carrinho2()
            indice = int(input(' Posição do produto:'))
            if indice < len(self.produtos):
                produto = self.produtos[indice]
                produto.set_qtd(8)
                print(' Objeto produto', self.produtos[indice])
                print(' Produto alterado')
            else:
                print(' Produto não está no carrinho!')




class Produto(object):
    def __init__(self, idt, descricao, preco=0.0, qtd=1):
        self.idt = idt
        self.preco = preco
        self.descricao = descricao
        self.qtd = qtd
    def get_nome_produto(self):
        return self.idt
    def get_preco(self):
        return self.preco
    def get_descricao(self):
        return self.descricao
    def get_qtd(self):
        return self.qtd
    def set_qtd(self, qtd):
        self.qtd = qtd
    def __str__(self):
        dados = f'Idt: {self.idt}, descrição: {self.descricao}, preço {self.preco}, qtd: {self.qtd}'
        return dados

if __name__ == '__main__':
    cliente1 = Cliente(123, 'Ailton')
    carrinho1 = CarrinhoCompra(12, cliente1)
    p1_arroz = Produto(1, 'Arroz', 29.90)
    p2_feijao = Produto(2, 'Feijão', 15.90, 2)
    p2_carne = Produto(3, 'Carne', 35.90, 3)
    print(carrinho1.get_num_pedido())
    print(carrinho1.get_cliente_nome())
    carrinho1.insere_produto(p1_arroz)
    carrinho1.insere_produto(p2_feijao)
    carrinho1.insere_produto(p2_carne)
    carrinho1.remove_produto2()
    #carrinho1.altera_qtd(p2_carne, 2)
    carrinho1.altera_qtd2()

    print(carrinho1.mostra_carrinho2())
    print(carrinho1.retorna_total())
    carrinho1.fecha_carrinho()
    carrinho1.fecha_carrinho2()