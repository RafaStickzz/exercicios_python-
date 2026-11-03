funcionarios = ["ana", "lucas", "beatriz", "carlos"]


for nome in funcionarios:
    
    email = f"{nome.strip().lower()}@arketech.com"
    print(f"Funcionário(a): {nome.title()} -> E-mail: {email}")