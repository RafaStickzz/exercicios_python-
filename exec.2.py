
while True: # o loop  infinito foi iniciado
    comando = input("Digite 'sair' para desligar o motor: ") # o usuário digita um comando

    if comando.lower() == 'sair':
        print("Motor desligado.")
        break # O loop foi interrompido(trava adicionada)
    else:
        print("o motor continua ligado...")