preço_empresa = float(input("Qual é o preço do produto que a empresa está oferecendo?: "))
if preço_empresa >= 100000:
    print("Aprovamos limite de até 20.000")
elif preço_empresa > 50000 and preço_empresa < 100000:
    print("Aprovamos limite de até 10.000")
else:
    print("Crédito reprovado, o valor do produto é muito baixo para aprovação de crédito.")