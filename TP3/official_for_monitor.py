import calendar


### 1. Concatenar Nome e Sobrenome
def concatenates_names():
    name = input("Digite o seu nome: ")
    surname = input("Digite o seu sobrenome: ")
    return name + " " + surname


### 2.  Validação de Nome e Sobrenome com split
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


### 3. Exibir Sobrenome, Nome
def format_name():
    full_name = input("Digite seu nome e sobrenome (ex: Maria Maia): ").strip()
    items = full_name.split()

    if len(items) != 2:
        return "Erro: Insira um nome e sobrenome."

    name, surname = items
    return f"{surname.upper()}, {name}"


### 4. Data em Formato Inteiro
def format_date():
    date = input("Digite uma data no formato dd/mm/aaaa: ").strip()
    items = date.split("/")

    if len(items) == 3:
        day, month, year = items
        print(f"Dia: {int(day)}, Mês: {int(month)}, Ano: {int(year)}")
    else:
        print("Erro: Formato de data inválido. Digite uma data no formato dd/mm/aaaa.")


### 5. Validação de Data
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


###6.Formato “dia de mês de ano”
def format_day_off_month():
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


### 7. Verificar Palíndromo
def check_is_palindrome():
    word = input("Digite uma palavra: ").strip().lower()

    if word == word[::-1]:
        print(f"A palavra '{word}' é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")


### 8. Contagem de Vogais
def count_vowels():
    phrase = input("Digite uma frase: ").strip()
    vowels = "aeiouAEIOU"
    count = 0

    for char in phrase:
        if char in vowels:
            count += 1

    print(f"'{phrase}' tem {count} vogais.")


### 9. Formatar Número de Telefone
def format_phone_number():
    phone_number = input("Digite um número de telefone (11 dígitos): ").strip()

    if len(phone_number) == 11 and phone_number.isdigit():
        ddd = phone_number[:2]
        formatted_number = f"({ddd}) {phone_number[2:7]}-{phone_number[7:]}"
        print(f"Número formatado: {formatted_number}")
    else:
        print("Erro: O número de telefone deve conter 11 dígitos.")


### 10.  Dia da Semana
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


### 11. Formatar CPF
def format_cpf():
    cpf = input("Digite um número de CPF (somente números): ").strip()

    if cpf.isdigit() and len(cpf) == 11:
        formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        print(f"CPF: {formatted_cpf}")
    else:
        print("Erro: O número de CPF deve conter exatamente 11 números.")


### 12. Inverter Frase com for
def invert_sentence():
    phrase = input("Digite uma frase: ").strip()

    inverted_phrase = ""
    for char in phrase:
        inverted_phrase = char + inverted_phrase

    print(f"Frase invertida: {inverted_phrase}")


### 13.Inverter Frase com Slicing
def invert_sentence():
    phrase = input("Digite uma frase: ").strip()

    inverted_phrase = phrase[::-1]

    print(f"Frase invertida: {inverted_phrase}")


### 14. Cinco Primeiros e Últimos Caracteres
def first_last_characters():
    phrase = input("Digite uma frase: ").strip()

    print(f"Cinco primeiros: {phrase[:5]}")
    print(f"Cinco últimos: {phrase[-5:]}")


### 15. Substituir “;” por “,”
def replace_semicolon():
    phrase = input("Digite uma frase com ';' no final: ").strip()

    print(phrase.replace(";", ","))


### 16. Cálculo de Média com f-strings
def calculate_average():
    average = (
        float(input("Digite um número: ")) + float(input("Digite outro número: "))
    ) / 2

    print(f"A média dos números é: {average:.2f}")


### Chamadas das funções:
# 1.
print(concatenates_names())
# 2.
validated_name = validate_entry()
print(f"Entrada válida: {validated_name}")
# 3.
formatted_name = format_name()
print(formatted_name)
# 4.
format_date()
# 5.
format_and_validate_date()
# 6.
format_day_off_month()
# 7.
check_is_palindrome()
# 8.
count_vowels()
# 9.
format_phone_number()
# 10.
day_of_week()
# 11.
format_cpf()
# 12.
invert_sentence()
# 13.
invert_sentence()
# 14.
first_last_characters()
# 15.
replace_semicolon()
# 16.
calculate_average()
