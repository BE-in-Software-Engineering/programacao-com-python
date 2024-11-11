# 16. Documentação com DocStrings


# Cria a função com a entrada do nome e das notas
def student_data():
    """
    Solicita o nome e as notas de um aluno.

    Caso o nome inserido seja 'FIM', o programa finaliza e retorna None para notas.
    Solicita duas notas e verifica se estão entre 0 e 10.
    Em caso de entrada inválida, pede as notas novamente.

    Returns:
        (str, float, float) O nome do aluno e suas duas notas.
        (str, None, None) caso 'FIM' seja digitado para finalizar.
    """
    name = input("Informe o nome do aluno: ")

    if name.upper() == "FIM":
        print("Programa finalizado")
        return name, None, None
    else:
        note1 = float(input("Digite a primeira nota: "))
        note2 = float(input("Digite a segunda nota: "))
        if not (0 <= note1 <= 10 and 0 <= note2 <= 10):
            print("Notas devem ser entre 0 e 10. Insira uma nota válida")
            return student_data()
        else:
            return name, note1, note2


# Função que calcula a média do aluno
def student_average_status(note1, note2):
    """
    Calcula a média de um aluno e determina o status de aprovação.

    Args:
        note1 (float): Primeira nota do aluno
        note2 (float): Segunda nota do aluno.

    Returns:
        (float, str) Média arredondada do aluno e o status de aprovação.
        Status é "aluno(a) aprovado(a)" se a média é >= 6. Caso contrário, "aluno(a) em prova final".
    """
    average = round((note1 + note2) / 2, 1)
    status = "aluno(a) aprovado(a)" if average >= 6 else "aluno(a) em prova final"
    return average, status


# Função que calcula e exibe a média da turma
def class_average():
    """
    Calcula e exibe a média da turma.
    Solicita os dados de cada aluno usando a função `student_data`, calcula e exibe a média e o status de cada aluno usando a função `student_average_status`.
    No final, exibe a média geral da turma.
    """
    general_average = 0
    student_count = 0

    while True:
        name, note1, note2 = student_data()

        if note1 is None and note2 is None:
            break

        average, status = student_average_status(note1, note2)
        print(f"{name} - Média: {average} ({status})")

        general_average += average
        student_count += 1

    if student_count > 0:
        class_average = round(general_average / student_count, 1)
        print(f"\nMédia da turma: {class_average}")


class_average()
