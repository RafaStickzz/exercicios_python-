print("========================")
print(" Status de credencial ")
print("========================")
print("")
credencial = input("Informe a sua credencial(ativa/bloqueada): ").strip().lower()
 
if credencial == "bloqueada":
    print("Credencial bloqueada")
   
elif credencial == "ativa":
    print("Credencial aceita")



