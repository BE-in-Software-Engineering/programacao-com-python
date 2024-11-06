import random


def create_history():
    characters = ["Um elfo", "Um grilo", "Um pássaro", "Um príncipe", "Um golfinho"]
    actions = ["cantou", "passeou", "viajou", "sonhou"]
    locations = ["em uma floresta", "em uma fazenda", "em um castelo", "em uma praia"]

    character, action, location = (
        random.choice(characters),
        random.choice(actions),
        random.choice(locations),
    )

    print(f"{character} {action} {location}.")


create_history()
