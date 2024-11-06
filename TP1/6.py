import random


def game():
    random_number = random.randint(1, 100)
    print("Tente advinhar um número entre 1 e 100.")

    while True:
        attempt = int(input("Digite seu palpite entre 1 e 100: "))

        if attempt < 1 or attempt > 100:
            print("Insira um número entre 1 e 100.")
            continue

        if attempt < random_number:
            print("Muito baixo! Tente novamente.")
        elif attempt > random_number:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {random_number}.")
            break


game()
