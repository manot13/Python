s = int(input("Digite os segundos: "))

dia = s//86400
hora = s//3600
minu = (s - (hora*3600))//60
segundos = s - (hora*3600) - (minu*60)

print("{:d} segundos corresponde a {:d} dia(s), {:d} hora(s), {:d} minuto(s) e {:d} segundo(s)." .format(s, dia, hora, minu, segundos))


