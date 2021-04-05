def escreverPratos():
    for i in range(0, t):
        op = int(input("\nEscolha o prato de sua preferência: "))
        if op == 1:
            vet.append("Bobó de Camarão")
            vetPrecoPrato.append(25.90)
        if op == 2:
            vet.append("Moqueca de Camarão")
            vetPrecoPrato.append(29.90)
        if op == 3:
            vet.append("Moqueca de Peixe")
            vetPrecoPrato.append(29.90)
        if op == 4:
            vet.append("Moqueca Mista")
            vetPrecoPrato.append(35.90)
        if op == 5:
            vet.append("Filet de Salmão")
            vetPrecoPrato.append(49.90)
        if op == 6:
            vet.append("Filet à Parmegiana")
            vetPrecoPrato.append(19.90)
        if op == 7:
            vet.append("Picanha Tropeiro")
            vetPrecoPrato.append(45.90)
        if op == 8:
            vet.append("Filet Mignon Recheado")
            vetPrecoPrato.append(39.90)

def escreverBebidas():
    for i in range(0, n):
        op2 = int(input("\nEscolha a bebida de sua preferência: "))
        if op2 == 1:
            vet.append("Suco de Laranja")
            vetPrecoBebida.append(4)
        if op2 == 2:
            vet.append("Suco de Maracujá")
            vetPrecoBebida.append(4)
        if op2 == 3:
            vet.append("Suco de Manga")
            vetPrecoBebida.append(4)
        if op2 == 4:
            vet.append("Refrigerante Coca-cola")
            vetPrecoBebida.append(3)
        if op2 == 5:
            vet.append("Refrigerante Guaraná")
            vetPrecoBebida.append(3)
        if op2 == 6:
            vet.append("Refrigerante Sprite")
            vetPrecoBebida.append(3)
        if op2 == 7:
            vet.append("Cerveja longneck")
            vetPrecoBebida.append(7)
            
def escreverSobremesas():
    for i in range (0, n):
        op3= int(input("\nEscolha a sobremesa de sua preferência: "))
        if op3 == 1:
            vet.append("Pudim de Chocolate")
            vetPrecoSobremesa.append(8)
        if op3 == 2:
            vet.append("Açai 500ml")
            vetPrecoSobremesa.append(15)      
        if op3 == 3:
            vet.append("Bolo de Banana")
            vetPrecoSobremesa.append(12)     
        if op3 == 4:
            vet.append("Milkshake Ovomaltine")
            vetPrecoSobremesa.append(9)
        if op3 == 5:
            vet.append("Petit Gateau")
            vetPrecoSobremesa.append(18)

def cardapioPratos():
    print("\n|1 – Bobó de Camarão - R$ 25,90|\nCamarão, creme de mandioca e arroz\n")
    print("|2 – Moqueca de Camarão - R$ 29,90|\nCamarão, pirão, arroz e farofa\n")
    print("|3 – Moqueca de Peixe - R$ 29,90|\nCação, arroz, pirão e farofa\n")
    print("|4 – Moqueca Mista - R$ 35,90|\nCamarão, caçã, pirão, arroz e farofa\n")
    print("|5 – Filet de Salmão - R$ 49,90|\nSalmão grelhado, arroz e fritas\n")
    print("|6 – Filet à Parmegiana - R$ 19,90|\nArroz branco, fritas e bife bovino empanado\n")
    print("|7 – Picanha Tropeiro - R$ 45,90|\nPicanha, arroz, farofa e feijão de corda\n")
    print("|8 – Filet Mignon Recheado - R$ 39,90|\nFilet milanesa, 3 queijos, presunto, arroz à grega e fritas\n\n")

def cardapioBebidas():
    print("\n\nSuco: |1 - Laranja|, |2 - Maracujá|, |3 - Manga| - |400ml| - |R$ 4,00|\n")
    print("Refrigerante lata: |4 - Coca-cola|, |5 - Guaraná|, |6 - Sprite| - |R$ 3,00|\n")
    print("|7 - Cerveja longneck| - |R$ 7,00|\n")

def cardapioSobremesas():
    print("\n|1 - Pudim de Chocolate - R$ 8,00|")
    print("\n|2 - Açai 500ml - R$ 15,00|")
    print("\n|3 - Bolo de Banana - R$ 12,00|")
    print("\n|4 - Milkshake Ovomaltine - R$ 9,00|")
    print("\n|5 - Petit Gateau - R$ 18,00|")

t = int(input("Digite quantos pratos você irá querer: "))
vet = []
vetPrecoPrato = []
vetPrecoBebida = []
vetPrecoSobremesa = []
somap=0
somapb=0
somapbs=0

for i in range(0, t):
    cardapioPratos()
    escreverPratos()
    break

for i in range(0, t):
    somap=somap+vetPrecoPrato[i]

opb = (input("\n\nGostaria de bebidas para acompanhar[s/n]? "))
if opb == 'sim' or opb == 's':
    n = int(input("\n\n\nDigite quantas bebidas você irá querer: "))
    for i in range(0, n):
        cardapioBebidas()
        escreverBebidas()
        break
    for i in range(0, n):
        somapb=somapb+vetPrecoBebida[i]
        
    ops = (input("\n\nGostaria de sobremesa após a refeição[s/n]? "))
    if ops == 'sim' or ops == 's':
        n= int(input("\n\n\nDigite quantas sobremesas você irá querer: "))
        for i in range (0, n):
            cardapioSobremesas()
            escreverSobremesas()
            break
        for i in range (0, n):
            somapbs=somapbs+vetPrecoSobremesa[i]

        somaTotal=somap+somapb+somapbs
        print("\n\nSeu pedido: %s" %vet)
        print("\nPreço total do seu pedido: R$ %.2f" %somaTotal)
    else:
        somaTotal=somap+somapb
        print("\n\nSeu pedido: %s" %vet)
        print("\nPreço total do seu pedido: R$ %.2f" %somaTotal)
else:
    ops = (input("\n\nGostaria de sobremesa após a refeição[s/n]? "))
    if ops == 'sim' or ops == 's':
        n= int(input("\n\n\nDigite quantas sobremesas você irá querer: "))
        for i in range (0, n):
            cardapioSobremesas()
            escreverSobremesas()
            break
        for i in range (0, n):
            somapbs=somapbs+vetPrecoSobremesa[i]
            
        somaTotal=somap+somapbs
        print("\n\nSeu pedido: %s" %vet)
        print("\nPreço total do seu pedido: R$ %.2f" %somaTotal)
    else:
        somaTotal=somap
        print("\n\nSeu pedido: %s" %vet)
        print("\nPreço total do seu pedido: R$ %.2f" %somaTotal)