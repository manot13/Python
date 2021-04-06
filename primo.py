num = int(input("Digite um número para verificar se é primo: "))
i = 2
result = 0

while(i <= (num/2)):
    i = i + 1 # 3
    if(num % 1 == 0): 
        result = result + 1 #1
        break


if(result == 0):
    print("Este número é primo!")
else:
    print("Este número não é primo!")
