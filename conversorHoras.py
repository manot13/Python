def conversao(n):
    if n > 12:
        novahora = n - 12
    return novahora

sair = 1

while sair != 0:
    hora = int(input("\nDigite a hora: "))
    minu = int(input("Digite os minutos: "))
    
    if hora == 24:
        print('%d:%d A.M' %(conversao(hora),minu))
    elif hora>12 and hora != 24:
        print('%d:%d P.M' %(conversao(hora),minu))
    else:
        print('%d:%d A.M' %(hora, minu))
    sair = int(input("\n\nSe quiser continuar, digite 1, se não digite 0: "))

