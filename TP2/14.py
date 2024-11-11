# 14. Entrada Validada de Números
def valid_number():
    while True:
        try:
            num = int(input("Digite um número maior ou igual a zero: "))
            if num >= 0:
                print(f"Você digitou o número {num}")
                return num
            else:
                print("O número deve ser maior ou igual a zero. Tente novamente.")
        except ValueError:
            print("Error: Entrada inválida.\nPor favor, digite um número inteiro.")


valid_number()
