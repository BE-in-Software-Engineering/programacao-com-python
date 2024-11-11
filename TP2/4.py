# 4. Tabuada de 1 a 10
for i in range(1, 11):
    print(f"Tabuada do {i}:")

    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")

    print("-" * 10)
