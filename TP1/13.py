def text_palindrome():
    text = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
    result = "É um palíndromo!" if text == text[::-1] else "Não é um palíndromo!"
    print(result)


text_palindrome()
