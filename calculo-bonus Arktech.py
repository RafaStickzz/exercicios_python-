# ==================================================
# MÓDULOS DE PROCESSAMENTO (def)
# ==================================================
def calcular_bonus(salario):
    """Calcula o bônus padrão de 15% da ArkTech"""
    return salario * 0.15


# ==================================================
# INTERFACE DO SISTEMA
# ==================================================
print("=" * 50)
print("           RH ARKTECH - BÔNUS INICIAL")
print("=" * 50)

while True:
    print("\n--- NOVO REGISTRO ---")

    nome = input("Nome completo (ou digite 0 para sair): ").strip()

    if nome == "0":
        print("\nEncerrando o painel de bônus. Bom trabalho!")
        break

    if not nome:
        print("ERRO: O campo de nome não pode ficar vazio.")
        continue

    cargo = input("Cargo contratado: ").strip()
    if not cargo:
        print("ERRO: O campo de cargo não pode ficar vazio.")
        continue

    try:
        salario = float(input("Salario Base (use ponto. Ex: 1500.00): R$ "))

        if salario <= 0:
            print("\nERRO LOGISTICO: O salario deve ser maior que zero.")
            print("Registro cancelado. Tente novamente.")
            continue

    except ValueError:
        print("\nERRO DE SINTAXE: Digite apenas números válidos (ex: 1500.00).")
        continue

    bonus = calcular_bonus(salario)
    total = salario + bonus

    print("\n--- RESUMO DO REGISTRO ---")
    print(f"Nome: {nome.title()}")
    print(f"Cargo: {cargo.title()}")
    print(f"Salário Base: R$ {salario:.2f}")
    print(f"Bônus (15%): R$ {bonus:.2f}")
    print(f"Total a receber: R$ {total:.2f}")
