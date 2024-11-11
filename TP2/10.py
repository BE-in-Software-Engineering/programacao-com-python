# 10. Números Maiores ou Iguais á Média
def create_list():
    seq_numbers = []
    while True:
        num = int(input("Digite um número inteiro (0 caso deseje finalizar): "))
        if num == 0:
            break
        seq_numbers.append(num)
    return seq_numbers


def larger_than_average(seq_numbers):
    average = sum(seq_numbers) / len(seq_numbers)

    filtered_numbers = []
    for number in seq_numbers:
        if number >= average:
            filtered_numbers.append(number)

    if filtered_numbers:
        print(f"Números maiores ou iguais à média: {filtered_numbers}")
    else:
        print("Não há números maiores ou iguais à média.")


seq_numbers = create_list()
larger_than_average(seq_numbers)
