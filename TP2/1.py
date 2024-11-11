# 1. Contando Vogais
def count_vowels():
    vowels = ["a", "e", "i", "o", "u"]
    character_sequence = ""
    count = 0

    while True:
        character = input("Digite um caractere (ou '.' para terminar):")
        if character == ".":
            break
        character_sequence += character

    for character in character_sequence:
        if character.lower() in vowels:
            count += 1

    print(f"Número de vogais: {count}")


count_vowels()
