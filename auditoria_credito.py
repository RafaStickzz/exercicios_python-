"""
Atividade Prática: Árvore de Decisão de Crédito (Caso ArkeTech)
Dupla: [Rafael Evaristo e Miguel Augusto]
 Copiloto: Gemini
"""
 
def auditoria_credito():
    print("--- Sistema de Triagem de Crédito - ArkeTech ---")
   
    # 1. Coleta de dados
    nome_empresa = input("Digite o nome da empresa solicitante: ")
    faturamento_mensal = float(input("Digite o faturamento mensal (R$): "))
    valor_emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))
   
    # 2. Processamento (Simulando o empréstimo dividido em 12 vezes sem juros)
    valor_parc = valor_emprestimo / 12
   
    # Cálculo do percentual com arredondamento para evitar pequenas imprecisões decimais
    percentual_comprometimento = round((valor_parc / faturamento_mensal) * 100, 2)
   
    # 3. Árvore de Decisão baseada nas Regras de Negócio
    if percentual_comprometimento <= 30.0:
        status = "APROVADO"
        mensagem = "O valor da parcela é menor ou igual a 30% do faturamento."
    elif percentual_comprometimento <= 50.0:
        status = "EM ANÁLISE (Risco Moderado)"
        mensagem = "O valor da parcela está entre 30,1% e 50% do faturamento."
    else:
        status = "RECUSADO"
        mensagem = "O valor da parcela é maior que 50% do faturamento."
       
    # 4. Saída formatada com f-strings
    print("\n" + "="*40)
    print(f"PARECER DE CRÉDITO - {nome_empresa.upper()}")
    print("="*40)
    print(f"Faturamento Mensal: R$ {faturamento_mensal:,.2f}")
    print(f"Valor do Empréstimo: R$ {valor_emprestimo:,.2f}")
    print(f"Valor da Parcela (12x): R$ {valor_parc:,.2f}")
    print(f"Comprometimento da Renda: {percentual_comprometimento:.2f}%")
    print(f"Status do Pedido: {status}")
    print(f"Motivo: {mensagem}")
    print("="*40)
 
if __name__ == "__main__":
    auditoria_credito()
 