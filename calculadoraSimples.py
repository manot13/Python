def Soma(a, b):
    return a+b
def Sub(i, j):
    return i-j
def Multi(l, k):
    return l*k
def Div(u, o):
    return u/o

print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')
print('0 - Sair')

op = int(input("\nEscolha qual opção: "))

while(op != 0):
    if (op == 1):
        x = int(input('\nDigite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        print(Soma(x, y))
        op = int(input("\nEscolha qual opção: "))
    if (op == 2):
        n = int(input('\nDigite o primeiro número: '))
        m = int(input('Digite o segundo número: '))
        print(Sub(n, m))
        op = int(input("\nEscolha qual opção: "))
    if (op == 3):
        p = int(input('\nDigite o primeiro número: '))
        q = int(input('Digite o segundo número: '))
        print(Multi(p, q))
        op = int(input("\nEscolha qual opção: "))
    if (op == 4):
        t = int(input('\nDigite o primeiro número: '))
        r = int(input('Digite o segundo número: '))
        if(r == 0):
            print("\nNão posso dividir por 0.")
            break;
        print(Div(t, r))
        op = int(input("\nEscolha qual opção: "))
    if (op != 1 and op != 2 and op != 3 and op != 4 and op != 0):
        print("\nEssa opção não existe!")
        break
    if (op == 0):
        print("\nVocê saiu!")
        break
