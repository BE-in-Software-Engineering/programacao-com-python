import random


def dice_game():
    number_dice = int(input("Quantos dados deseja lançar? "))

    results = []
    for _ in range(number_dice):
        results.append(random.randint(1, 6))

    print(f"Resultados: {results}")


dice_game()
