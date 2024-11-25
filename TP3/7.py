# 7. Verificar Palíndromo
def check_is_palindrome():
    word = input("Digite uma palavra: ").strip().lower()

    if word == word[::-1]:
        print(f"A palavra '{word}' é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")


check_is_palindrome()
