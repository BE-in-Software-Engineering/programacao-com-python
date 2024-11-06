def greeting():
    name = input("Digite seu nome: ")
    surname = input("Digite seu sobrenome: ")

    template = f"Olá, {name} {surname}. Bem-vindo(a)!"

    print(template)


greeting()
