# 5. Progressão Aritmética
def arithmetic_progression(first_term, second_term, num_terms=10):
    reason = second_term - first_term

    terms = [first_term, second_term]
    for i in range(2, num_terms):
        next_term = terms[-1] + reason
        terms.append(next_term)

    return terms


first_term = int(input("Digite o primeiro número (primeiro termo da PA): "))
second_term = int(input("Digite o segundo número (segundo termo da PA): "))

if second_term <= first_term:
    print("O segundo número deve ser maior que o primeiro para gerar uma PA.")
else:
    terms = arithmetic_progression(first_term, second_term)

    print(f"A sequência gerada em PA é: {terms}")
