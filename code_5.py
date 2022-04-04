def approvedOrNot():
    grade1 = float(input("Digite a primeira nota: ").replace(",", "."))
    grade2 = float(input("Digite a segunda nota: ").replace(",", "."))
    averageGrade = round((grade1 + grade2) / 2)
    if(averageGrade >= 7):
        print("Aprovado")
    elif(averageGrade < 7):
        print("Reprovado")
    elif(averageGrade == 10):
        print("Aprovado com Distinção")

approvedOrNot()