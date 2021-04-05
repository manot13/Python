#Faça um programa para registro de animais(cachorro, gato) utilizando herança. O PetShop que gerenciará o sistema terá que ter um controle das características do animal para facilitar os registros de cada animal, como categoria, cor, nome raça, tipo de focinho(cachorro) e cor
#dos olhos(gato). Cada cliente também terá que ter uma conta cadastrada no petshop e terá que logar nela para registrar seu animal.

class Animal(object):
    def __init__(self, categoria, cor):
        self._categoria = categoria
        self._cor = cor

    @property
    def categoria(self):
        return categoria
    @property
    def cor(self):
        return cor

    def exibir_dados(self):
        print(f"\nCategoria do animal: {self.categoria}")
        print(f"\nCor do animal: {self.cor}")

class Cachorro(Animal):
    def __init__(self, categoria, cor, nome, raca, focinhoTipo):
        super().__init__(categoria, cor)
        self._nome = nome
        self._raca = raca
        self._focinhoTipo = focinhoTipo

    @property
    def categoria(self):
        return categoria

    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def raca(self):
        return self._raca
    @raca.setter
    def raca(self, raca):
        self._raca = raca

    @property
    def focinhoTipo(self):
        return self._focinhoTipo
    @focinhoTipo.setter
    def focinhoTipo(self, focinhoTipo):
        self._focinhoTipo = focinhoTipo

    def exibir_dados(self):
        print(f"\nCategoria do animal: {self.categoria}")
        print(f"Cor do cachorro: {self.cor}")
        print(f"Nome do cachorro: {self.nome}")
        print(f"Raça do cachorro: {self.raca}")
        print(f"Tipo de focinho do cachorro: {self.focinhoTipo}")

    def atualizar(self):
        while True:
            print("\n|1 - Atualizar cor|")
            print("|2 - Atualizar nome|")
            print("|3 - Atualizar raça|")
            print("|4 - Atualizar focinho|")
            print("|5 - Sair|\n")
            op = int(input("Escolha uma opção: "))
            if op == 1:
                novaCor = input("\nDigite a nova cor: ")
                self.cor = novaCor
            if op == 2:
                novoNome = input("\nDigite o novo nome: ")
                self.nome = novoNome
            if op == 3:
                novaRaca = input("\n Digite a nova raça: ")
                self.raca = novaRaca
            if op == 4:
                novoFocinho = input("\nDigite o novo tipo de focinho: ")
                self.focinhoTipo = novoFocinho
            if op == 5:
                break
            if op > 5 or op < 1:
                print("Opção inválida!")


class Gato(Animal):
    def __init__(self, categoria, cor, nome, raca, olhoCor):
        super().__init__(categoria, cor)
        self._nome = nome
        self._raca = raca
        self._olhoCor = olhoCor

    @property
    def categoria(self):
        return categoria

    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def raca(self):
        return self._raca
    @raca.setter
    def raca(self, raca):
        self._raca = raca

    @property
    def olhoCor(self):
        return self._olhoCor
    @olhoCor.setter
    def olhoCor(self, olhoCor):
        self._olhoCor = olhoCor

    def exibir_dados(self):
        print(f"\nCategoria do animal: {self.categoria}")
        print(f"Cor do gato: {self.cor}")
        print(f"Nome do gato: {self.nome}")
        print(f"Raça do gato: {self.raca}")
        print(f"Cor dos olhos do gato: {self.olhoCor}")

    def atualizar(self):
        while True:
            print("\n|1 - Atualizar cor|")
            print("|2 - Atualizar nome|")
            print("|3 - Atualizar raça|")
            print("|4 - Atualizar cor dos olhos|")
            print("|5 - Sair|\n")
            op = int(input("Escolha uma opção: "))
            if op == 1:
                novaCor = input("\nDigite a nova cor: ")
                self.cor = novaCor
            if op == 2:
                novoNome = input("\nDigite o novo nome: ")
                self.nome = novoNome
            if op == 3:
                novaRaca = input("\n Digite a nova raça: ")
                self.raca = novaRaca
            if op == 4:
                novaCorOlho = input("\nDigite a nova cor dos olhos: ")
                self.olhoCor = novaCorOlho
            if op == 5:
                break
            if op > 5 or op < 1:
                print("Opção inválida!")

def login():
    global email, senha
    print("\n|1 - Cadastrar-se|")
    print("|2 - Entrar|\n")
    op = int(input("Digite a opção: "))
    if op == 1:
        email = input("\nDigite um email: ")
        senha = input("Digite uma senha: ")
        print("\nCadastro efetuado com sucesso!")
        login()
    elif op == 2:
        acesso = input("\nUsuário: ")
        acesso2 = input("Senha: ")
        if 'email' not in globals() and 'senha' not in globals() or senha != acesso2 or email != acesso:
            print("\nSenha ou usuário inválidos!")
            login()
        elif acesso == email and acesso2 == senha:
            print("\nLogado com sucesso! Bem-vindo!")
            #início da inserção de dados
    elif op != 1 or op != 2:
        print("\nOpção inválida!")
        login()

if __name__ == '__main__':
    login()
    while True:
        categoria = input("\nDigite o seu tipo de animal: ")
        if categoria == 'cachorro' or categoria == 'Cachorro':
            cor = input("Digite a cor do seu animal: ")
            nome = input("Digite um nome para o seu animal: ")
            raca = input("Digite a raça do seu animal: ")
            focinhoTipo = input("Digite o tipo do focinho do seu cachorro: ")
            a1 = Cachorro(categoria, cor, nome, raca, focinhoTipo)
            a1.exibir_dados()
            a1.atualizar()
            a1.exibir_dados()
        elif categoria == 'gato' or categoria == 'Gato':
            cor = input("Digite a cor do seu animal: ")
            nome = input("Digite um nome para o seu animal: ")
            raca = input("Digite a raça do seu animal: ")
            olhoCor = input("Digite a cor dos olhos do seu gato: ")
            a1 = Gato(categoria, cor, nome, raca, olhoCor)
            a1.exibir_dados()
            a1.atualizar()
            a1.exibir_dados()
        else:
            print("\nEssa categoria não existe!")
        op = input("\nConfirmar dados [s/n]? ")
        if op == 's':
            print("\nObrigado e volte sempre!")
            break
        else:
            continue