print ("======================")
print ("ESTOQUE DE PRODUTOS   ")
print ("======================")
print("")
estoque = int(input("informe a quanidade de produtos no estoque: "))
if estoque <16:
    print("COMPRA URGENTE")
if estoque >16 and estoque < 50:
    print("ESTOQUE REGULAR")
if estoque > 50:
    print("ESTOQUE CHEIO")