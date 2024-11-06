def voting():
    votes = [0, 0, 0]

    while True:
        option = input("Digite 1, 2 ou 3 para votar (ou 'fim' para terminar): ")

        if option == "1":
            votes[0] += 1
        elif option == "2":
            votes[1] += 1
        elif option == "3":
            votes[2] += 1
        elif option.lower() == "fim":
            break
        else:
            print("Opção inválida! Tente novamente.")

    print("\nResultado final dos votos:")
    print(f"Opção 1: {votes[0]} votos")
    print(f"Opção 2: {votes[1]} votos")
    print(f"Opção 3: {votes[2]} votos")


voting()
