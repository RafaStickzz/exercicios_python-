senha = "Admin123"
tentativas = 1
max_tentativas = 3
 
while tentativas <= max_tentativas:
    print(f"Tentativas {tentativas} de {max_tentativas}")
    senha_digitada = input("Digite a sua senha: ")
    if senha_digitada == senha:
     print("Acesso liberado")
     break
    else:
     print("Senha INCORRETA")
     print("Tente novamente")
     tentativas += 1
else:
    print("Acesso bloqueado")