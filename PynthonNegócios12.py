
vendas_trimestre = [12000.00, 15000.00, 18000.00]

total_faturamento = 0.0

for venda in vendas_trimestre:
    total_faturamento += venda 

print(f"O faturamento total do último trimestre foi: R$ {total_faturamento:,.2f}")
