# 12. Inverter Frase com for
def invert_sentence():
    phrase = input("Digite uma frase: ").strip()

    inverted_phrase = ""
    for char in phrase:
        inverted_phrase = char + inverted_phrase

    print(f"Frase invertida: {inverted_phrase}")


invert_sentence()
