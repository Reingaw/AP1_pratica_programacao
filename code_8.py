isOver = 0
grades = []

def printValues(grades):
    txt = ""
    for grade in grades:
        txt += f"{grade} "
    print(f"Notas digitadas: \n{txt}")

def printValuesReverse(grades):
    grades.sort(reverse=True)
    print("Notas digitadas em ordem reversa:")
    for grade in grades:
        print(grade)

def printSumValues(grades):
    sum = 0
    for grade in grades:
        sum += float(grade)
    print(f"Soma das notas digitadas: {sum}")

def printAverage(grades):
    sum = 0
    for grade in grades:
        sum += float(grade)
        average = round(sum / len(grades), 2)
    print(f"Média das notas: {average}")
    printQtUpDownAverage(grades, average)

def printQtUpDownAverage(grades, average):
    qtUp = 0
    qtDown = 0
    for grade in grades:
        if float(grade) > average:
            qtUp += 1
        elif float(grade) < average:
            qtDown += 1
    print(f"Quantidade de notas acima da média: {qtUp}")
    print(f"Quantidade de notas abaixo da média: {qtDown}")

while not isOver:
    value = input("Digite -1 para sair ou \n"
                        "Digite uma nota: ").replace(",", ".")
    if value != "-1":
        grades.append(value)
    else:
        isOver = 1
        print(f"Quantidade de notas digitadas: {len(grades)}")
        printValues(grades)
        printValuesReverse(grades)
        printSumValues(grades)
        printAverage(grades)
        print("\nPrograma Encerrado com sucesso...")