def calculator():
    operation = input("Escolha a operação (+, -, *, /): ")
    number1 = float(input("Digite o primeiro número: "))
    number2 = float(input("Digite o segundo número: "))

    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            result = "Não é possível realizar uma divisão por 0."
        else:
            result = number1 / number2
    else:
        result = "Escolha uma operação válida."

    print(f"Resultado da operação: {result}")


calculator()
