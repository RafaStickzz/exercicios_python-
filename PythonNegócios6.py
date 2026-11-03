
faltas = int(input("Digite o número de faltas injustificadas: "))
vendas = float(input("Digite o valor total de vendas: R$ "))


if faltas == 0 and vendas > 50000:
    print("PLR Aprovada")
else:
    print("PLR Negada")
