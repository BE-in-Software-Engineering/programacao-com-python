# 9. Números em Ordem Invertida
def create_list():
    seq_numbers = []
    while True:
        num = int(input("Digite um número inteiro (0 caso deseje finalizar): "))
        if num == 0:
            break
        seq_numbers.append(num)
    return seq_numbers


def invert_list(seq_numbers):
    seq_numbers.reverse()
    print("Sequência de números na ordem invertida:", seq_numbers)


seq_numbers = create_list()
invert_list(seq_numbers)
