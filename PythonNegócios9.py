
while True:
    matricula = input("Digite a matrícula do funcionário para bater o ponto: ").strip()
    
   
    if matricula == "0000":
        print("Sistema encerrado para manutenção.")
        break 
        
    
    print(f"Ponto batido com sucesso para a matrícula: {matricula}!")
    print("-" * 30)  
