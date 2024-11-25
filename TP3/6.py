# 6.Formato “dia de mês de ano”


def format_date():
    month_pt = [
        "",
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]

    date = input("Digite uma data no formato dd/mm/aaaa: ").strip()
    items = date.split("/")

    if len(items) != 3:
        print("Erro: Digite uma data no formato dd/mm/aaaa.")
        return

    day, month, year = items
    day, month, year = int(day), int(month), int(year)

    if not (1 <= month <= 12):
        print("Erro: Mês fora do intervalo de 1 a 12.")
        return

    month_name = month_pt[month].lower()

    # Dia formatado com dois digitos
    print(f"{day:02d} de {month_name} de {year}")


format_date()
