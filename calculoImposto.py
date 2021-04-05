def somaImposto(taxaImposto, custo):
    taxaImposto = (taxaImposto*custo)/100
    return taxaImposto+custo

taxa = int(input("Digite a taxa do imposto em porcentagem: "))
preco = int(input("Digite o preço original do produto: "))

print("\nPreço total: R$ %d" %somaImposto(taxa, preco))
