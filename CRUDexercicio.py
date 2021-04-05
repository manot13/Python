l = []
def menu():
    print("C = Create")
    print("R = Read")
    print("U = Update")
    print("D = Delete")
    print("Z = Sair")
    op = input("\nDigite qual opção você quer com a letra dela: ")
    if op == 'c' or op == 'C':
        create()
    elif op == 'r' or op == 'R':
        read()
    elif op == 'd' or op == 'D':
        delete()
    elif op == 'u' or op == 'U':
        update()
    elif op == 'z' or op == 'Z':
        print("Você saiu!")
        return 0
    else:
        print("\nOpção inválida! Tente novamente!\n")
        menu()

def lista_vazia():
    if len(l) == 0:
        print("Lista vazia!")
    return False

def create():
    print("[P] - Posição")
    print("[F] - Final")
    print("[S] - Sair")
    op = input("Opção: ")
    if op == 'p':
        i = int(input("Posição ou [-1] para sair: "))
        while i != -1:
            n = input("Nome: ")
            l.insert(i, n)
            i = int(input("Posição ou [-1] para sair: "))
    elif op == 'f':
        n = input("Nome ou <enter> para sair: ")
        while n != '':
            l.append(n)
            n = input("Nome ou <enter> para sair: ")
    elif op == 's':
        pass
    else:
        print("Opção inválida!")
    menu()

def read():
    if len(l) != 0:
        print(l)
        for i, v in enumerate(l):
            print(i, '--', v)
    lista_vazia()

def delete():
    if len(l) != 0:
        read()
        valor = int(input("Digite o valor que deseja excluir: "))
        if valor in l:
            l.remove(valor)
        else:
            print("Valor não existe!")
    lista_vazia()
    menu()

def update():
    if len(l) != 0:
        read()
        valor3 = int(input("Insira a posição que deseja colocar: "))
        valor2 = int(input("Insira o valor que deseja colocar: "))
        try:
            l[valor3]=valor2
        except:
            print("Valor não encontrado na lista!")
    lista_vazia()
    menu()

if __name__ == '__main__':
    menu()
