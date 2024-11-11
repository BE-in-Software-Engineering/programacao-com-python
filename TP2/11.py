# 11. Busca de Elemento na Lista
def search_element_in_list(number, arr):
    if number in arr:
        return arr.index(number)
    else:
        return -1


arr = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]
number = int(input("Digite um número: "))
index_element = search_element_in_list(number, arr)

if index_element != -1:
    print(f"O número {number} foi encontrado na posição {index_element} da lista.")
else:
    print(f"O número {number} não foi encontrado na lista.")
