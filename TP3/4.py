# 4. Data em Formato Inteiro
def format_date():
    date = input("Digite uma data no formato dd/mm/aaaa: ").strip()
    items = date.split("/")

    if len(items) == 3:
        day, month, year = items
        print(f"Dia: {int(day)}, Mês: {int(month)}, Ano: {int(year)}")
    else:
        print("Erro: Formato de data inválido. Digite uma data no formato dd/mm/aaaa.")


format_date()
