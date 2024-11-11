# 13. Separação de Pares e Ímpares
def is_even_or_odd(num):
    if num % 2 == 0:
        return "par"
    else:
        return "ímpar"


def create_lists(arr):
    even_numbers = []
    odd_numbers = []

    for num in arr:
        if is_even_or_odd(num) == "par":
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers


arr = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
even_numbers, odd_numbers = create_lists(arr)

print(f"Lista de números pares: {even_numbers}")
print(f"Lista de números ímpares: {odd_numbers}")
