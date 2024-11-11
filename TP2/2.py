# 2. Soma e Média de 1 a 100
def sum_and_average():
    first_term = 1
    last_term = 100
    total_terms = last_term

    sum_numbers = total_terms * (first_term + last_term) // 2
    average = sum_numbers / total_terms
    
    print(f"Soma de 1 a 100: {sum_numbers}")
    print(f"Média de 1 a 100: {average}")


sum_and_average()
