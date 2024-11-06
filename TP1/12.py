def word():
    word = input("Digite uma palavra: ")
    print(f"A palavra '{word}' é {'curta' if len(word) < 5 else 'longa'}.")


word()
