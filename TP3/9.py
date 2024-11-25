# 9. Formatar Número de Telefone
def format_phone_number():
    phone_number = input("Digite um número de telefone (11 dígitos): ").strip()

    if len(phone_number) == 11 and phone_number.isdigit():
        ddd = phone_number[:2]
        formatted_number = f"({ddd}) {phone_number[2:7]}-{phone_number[7:]}"
        print(f"Número formatado: {formatted_number}")
    else:
        print("Erro: O número de telefone deve conter 11 dígitos.")


format_phone_number()
