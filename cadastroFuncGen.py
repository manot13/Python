class Funcionario(object):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def mostra_dados(self):
        print(f"\nNome: {self._nome}")
        print(f"CPF: {self._cpf}")
        print(f"Salário: R$ {self._salario}")

    def bonificacao(self):
        print(f"A bonificação é de R$ {self._salario * 0.1}")
        self._salario = self._salario * 1.1
        print(f"O salário após a bonificação é de R$ {self._salario}")
        return

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qt_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qt_funcionarios = qt_funcionarios

    def mostra_dados(self):
        print(f"\nNome: {self._nome}")
        print(f"CPF: {self._cpf}")
        print(f"Salário: R$ {self._salario}")
        print(f"Quantidade de funcionários: {self._qt_funcionarios}")

    def bonificacao_gerente(self):
        print(f"A bonificação é de R$ {self._salario * 0.15}")
        self._salario = self._salario * 1.15
        print(f"O salário após a bonificação é de R$ {self._salario}")
        return

    def autentica(self):
        while True:
            acesso = input("\nDigite a senha:")
            if acesso == senha:
                print(f"\nAcesso realizado com sucesso. Bem-vindo, {self._nome}.")
                break
            else:
                continuar = input(f"\nSenha incorreta! Deseja tentar novamente? S ou N ")
                if continuar == "N" or continuar == "n" or continuar == "NÃO" or continuar == "NAO" or continuar == "Não" or continuar == "Nao" or continuar == "não" or continuar == "nao":
                    break

if __name__ == '__main__':
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    salario = float(input("Digite o salário (em R$) do funcionário: "))
    f1 = Funcionario(nome, cpf, salario)
    f1.mostra_dados()
    f1.bonificacao()


    nome = input("\nDigite o nome do gerente: ")
    cpf = input("Digite o CPF do gerente: ")
    salario = float(input("Digite o salário (em R$) do gerente: "))
    senha = input("Digite a senha de acesso: ")
    qt_funcionarios = int(input("Digite a quantidade de funcionários: "))
    g1 = Gerente(nome, cpf, salario, senha, qt_funcionarios)
    g1.autentica()
    g1.mostra_dados()
    g1.bonificacao_gerente()