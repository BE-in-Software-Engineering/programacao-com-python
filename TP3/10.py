# 10.  Dia da Semana
def day_of_week():
    days = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }

    try:
        number = int(input("Digite um número de 1 a 7: "))
        if 1 <= number <= 7:
            print(days[number])
        else:
            print("Erro: número inválido")

    except ValueError:
        print("Erro: número inválido")


day_of_week()
