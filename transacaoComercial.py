compra = float(input("Digite preço de compra: "))
venda = float(input("Digite preço de venda: "))

lucro = venda-compra
preju = compra-venda


if (compra<venda):
    print("Teve lucro.")
    print("Total do lucro: R$", lucro)
elif(compra>venda):
    print("Teve prejuízo.")
    print("Total do prejuízo: R$", preju)
else:
    print("Os valores são iguais.")
