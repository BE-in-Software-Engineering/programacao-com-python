def addition(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


def inter_division(a, b):
    return a // b


a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))

print("Soma:", addition(a, b))
print("Subtração:", sub(a, b))
print("Multiplicação:", multiply(a, b))
print("Divisão:", division(a, b))
print("Divisão inteira:", inter_division(a, b))
