n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))

result = n1-n2
ct=1

while(result!=0):
    result = result - n2
    ct+=1

if(n2<=0 or n1<0):
    print("Não é possível efetuar a operação por zero ou números negativos.")
else:
    print("%d" %ct)
