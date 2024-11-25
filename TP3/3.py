# 3. Exibir Sobrenome, Nome
def format_name():
    full_name = input("Digite seu nome e sobrenome (ex: Maria Maia): ").strip()
    items = full_name.split()

    if len(items) != 2:
        return "Erro: Insira um nome e sobrenome."

    name, surname = items
    return f"{surname.upper()}, {name}"


formatted_name = format_name()
print(formatted_name)
