# 8. Soma de Duas Listas
arr_1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr_2 = [10, 20, 30, 40, 50, 60, 70, 80]


sum_elements = []

for i in range(len(arr_1)):
    sum_elements.append(arr_1[i] + arr_2[i])

print("A soma das listas é:", sum_elements)
