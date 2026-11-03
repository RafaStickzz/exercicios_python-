
regiao = input("Digite a sigla da região (S, SE, CO, NE, N): ").strip().upper()

match regiao:
    case "S" | "SE":
        frete = 15.00
        print(f"O valor do frete para a região {regiao} é: R$ {frete:.2f}")
    case "CO":
        frete = 25.00
        print(f"O valor do frete para a região {regiao} é: R$ {frete:.2f}")
    case "NE" | "N":
        frete = 35.00
        print(f"O valor do frete para a região {regiao} é: R$ {frete:.2f}")
    case _:
        print("Região inválida! Digite uma das siglas informadas (S, SE, CO, NE, N).")
