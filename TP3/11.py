# 11. Formatar CPF
def format_cpf():
    cpf = input("Digite um número de CPF (somente números): ").strip()

    if cpf.isdigit() and len(cpf) == 11:
        formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        print(f"CPF: {formatted_cpf}")
    else:
        print("Erro: O número de CPF deve conter exatamente 11 números.")


format_cpf()
