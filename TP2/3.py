# 3. Fatorial de Números Positivos
def calculate_factorial(number):
    factorial = 1
    count = 2

    if number == 0 or number == 1:
        return 1

    while count <= number:
        factorial *= count
        count += 1

    return factorial


def main():
    while True:
        number = int(input("Digite um número inteiro positivo (ou 0 para sair): "))

        if number == 0:
            print("Finalizado.")
            break

        elif number > 0:
            print(f"O fatorial de {number} é {calculate_factorial(number)}.")
        else:
            print("Por favor, digite um número inteiro positivo.")


main()
