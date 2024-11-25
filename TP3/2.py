# 2.  Validação de Nome e Sobrenome com split
def validate_entry():
    while True:
        full_name = input("Digite seu nome e sobrenome.\n(Ex: Maria Castro): ").strip()
        items = full_name.split()

        if len(items) == 2:
            name, surname = items
            if len(name) >= 2 and len(surname) >= 2:
                return full_name

        print(
            "Erro: Entrada inválida. Insira um nome e sobrenome com o minimo de dois caracteres cada."
        )


validated_name = validate_entry()
print(f"Entrada válida: {validated_name}")
