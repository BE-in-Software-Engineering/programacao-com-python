def bmi():
    weight = float(input("Peso (kg): "))
    height = float(input("Altura (m): "))

    bmi = weight / (height**2)
    print(f"Seu IMC é: {bmi:.2f}")

    if bmi < 18.5:
        print("Abaixo do peso.")
    elif bmi < 24.9:
        print("Peso normal.")
    elif bmi < 29.9:
        print("Sobrepeso.")
    elif bmi < 39.9:
        print("Obesidade.")
    else:
        print("Obesidade grave.")


bmi()
