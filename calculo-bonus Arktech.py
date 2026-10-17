# ====================================================
# MÓDULOS DE PROCESSAMENTO (def)
# ====================================================
def calcular_bonus(salario):
    """Calcula o bônus padrão de 15% da ArkTech"""
    return salario * 0.15

# ====================================================
# INTERFACE DO SISTEMA
# ====================================================
print("===================================================")
print("          RH ARKTECH - BÔNUS INICIAL               ")
print("===================================================")

while True:
    print("\n--- NOVO REGISTRO ---")

    # O .strip() remove espaços em branco digitados sem querer
    nome = input("Nome completo (ou digite "0" para sair): ").strip()"

if nome == "0":
    print("\n   Encerrando o painel de bônus. Bom trabalho!")
    break

# Blindagem 1: Impede que o nome fique em branco se o usuario só apertar "Enter"
if not nome:
    print(" ERRO: O campo de nome não pode ficar vazio.")
    continue

cargo = input("Cargo contratado: ").strip()

# Blindagem 2: A Zona de Perigo (Tratamento de Exceções)
try:
    salario = float(input("Salario Base (use ponto. Ex: 1500.00): R$ "))

    # Blindagem 3: Regra de Negocio (Não existe salario negativo ou zero)
    if salario <= 0:
        print("\n  ERRO LOGISTICO: O salario deve ser maior que zero.")
        print("Registro cancelado. Tente novamente.")
        continue

except ValueError:
    print("\n  ERRO DE SINTAXE: Digite apenas ")