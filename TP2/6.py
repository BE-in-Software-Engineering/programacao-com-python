# 6. Números Primos em um Intervalo
def check_is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def find_primes(lower_range, upper_range):
    primes = []

    for num_prime in range(lower_range, upper_range + 1):
        if check_is_prime(num_prime):
            primes.append(num_prime)
    return primes


lower_range = int(input("Digite um número que corresponte ao intervalo inferior: "))
upper_range = int(input("Digite um número que corresponte ao intervalo superior: "))

prime_numbers_found = find_primes(lower_range, upper_range)

if prime_numbers_found:
    print(
        f"Números primos encontrados no intervalo de {lower_range} a {upper_range}: {prime_numbers_found}"
    )
    print(f"Quantidade de números primos encontrados: {len(prime_numbers_found)}")
else:
    print(
        f"Não foram encontrados números primos no intervalo de {lower_range} a {upper_range}."
    )
