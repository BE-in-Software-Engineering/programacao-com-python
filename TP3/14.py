# 14. Cinco Primeiros e Últimos Caracteres
def first_last_characters():
    phrase = input("Digite uma frase: ").strip()

    print(f"Cinco primeiros: {phrase[:5]}")
    print(f"Cinco últimos: {phrase[-5:]}")


first_last_characters()
