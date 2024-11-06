def create_name(firstName, secondName):
    name1 = firstName[:4].capitalize()
    name2 = secondName[2:] if len(secondName) >= 3 else secondName

    return name1 + name2


firstName = input("Digite um nome: ")
secondName = input("Digite outro nome: ")

name_created = create_name(firstName, secondName)
print(f"Novo nome: {name_created}")
