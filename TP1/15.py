def interactive_choice():
    print("Você vai tomar café da manhã. O que deseja comer?")

    choice = input("1 - Pão com calabresa\n2 - Pão na chapa\nEscolha (1 ou 2): ")

    if choice == "1":
        print("Você escolheu pão com calabresa.")
    elif choice == "2":
        print("Você escolheu pão na chapa.")
    else:
        print("Escolha inválida.")


interactive_choice()
