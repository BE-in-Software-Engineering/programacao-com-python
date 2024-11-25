# 8. Contagem de Vogais
def count_vowels():
    phrase = input("Digite uma frase: ").strip()
    vowels = "aeiouAEIOU"
    count = 0

    for char in phrase:
        if char in vowels:
            count += 1

    print(f"'{phrase}' tem {count} vogais.")


count_vowels()
