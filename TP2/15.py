# 15. Cálculo de Médias de Alunos
def student_data():
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


def student_average_status(note1, note2):
    average = round((note1 + note2) / 2, 1)
    status = "aluno(a) aprovado(a)" if average >= 6 else "aluno(a) em prova final"
    return average, status


def class_average():
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
