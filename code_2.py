def averageGrade():
    grade1 = float(input('Digite a primera nota: '))
    grade2 = float(input('Digite a segunda nota: '))
    grade3 = float(input('Digite a terceira nota: '))
    grade4 = float(input('Digite a quarta nota: '))
    result = (grade1 + grade2 + grade3 + grade4) / 4
    print(round(result, 2))

averageGrade()