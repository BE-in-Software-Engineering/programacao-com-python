# 12. Estatisticas de uma lista
def statistics(arr):
    min_value = min(arr)
    max_value = max(arr)
    total_sum = sum(arr)
    average = total_sum / len(arr)

    print(
        f"""
Estatísticas da Lista:
Menor número: {min_value}
Maior número: {max_value}
Soma dos números: {total_sum}
Média dos números: {average}
"""
    )


arr = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
statistics(arr)
