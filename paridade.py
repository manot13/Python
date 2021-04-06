a = int(input("Digite um número: "))

if a%2 == 0:
    print("Este número é par!")
else:
    print("Este número é ímpar!")

if a%5 == 0:
    print("Este número é múltiplo de 5!")
else:
    print("Este número não é múltiplo de 5!")

print("Número digitado: ", a)
print("Resto da divisão por 2: ", a%2)
print("Resto da divisão por 5: ", a%5)
