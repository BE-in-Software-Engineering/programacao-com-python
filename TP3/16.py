# 16. Cálculo de Média com f-strings
def calculate_average():
    average = (
        float(input("Digite um número: ")) + float(input("Digite outro número: "))
    ) / 2

    print(f"A média dos números é: {average:.2f}")


calculate_average()
