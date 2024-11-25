# 5. Validação de Data
import calendar


def format_and_validate_date():
    date = input("Digite uma data no formato dd/mm/aaaa: ").strip()
    items = date.split("/")

    if len(items) != 3:
        print("Erro: Digite uma data no formato dd/mm/aaaa.")
        return

    day, month, year = items
    day, month, year = int(day), int(month), int(year)
    print(f"Dia: {day}, Mês: {month}, Ano: {year}")

    if not (1 <= month <= 12):
        print("Erro: Mês fora do intervalo de 1 a 12.")
        return

    # Retorna uma tupla (segundo item da tupla - dia do mês)
    days_in_month = calendar.monthrange(year, month)[1]

    if not (1 <= day <= days_in_month):
        print(f"Erro: Data inválida. Este mês possui o máximo de {days_in_month} dias.")
        return

    print("Data válida.")


format_and_validate_date()
