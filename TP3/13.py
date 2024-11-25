# 13.Inverter Frase com Slicing
def invert_sentence():
    phrase = input("Digite uma frase: ").strip()

    inverted_phrase = phrase[::-1]

    print(f"Frase invertida: {inverted_phrase}")


invert_sentence()
