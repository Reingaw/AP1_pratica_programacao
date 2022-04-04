def salaryIncrease():
    salaryBase = float(input("Digite o salário: ").replace(",", "."))
    if salaryBase <= 280:
        calculateIncrease(salaryBase, 20)
    elif salaryBase > 280 and salaryBase < 700:
        calculateIncrease(salaryBase, 15)
    elif salaryBase > 700 and salaryBase < 1500:
        calculateIncrease(salaryBase, 10)
    elif salaryBase > 1500:
        calculateIncrease(salaryBase, 5)

def calculateIncrease(salaryBase, value):
    percent = value
    increaseValue = salaryBase * (percent / 100)
    newSalary = salaryBase + increaseValue
    print(f"Salário antes do reajuste: R${salaryBase}")
    print(f"Percentual Aplicado: {percent}%")
    print(f"Valor do aumento: R${increaseValue}")
    print(f"Salário após o reajuste: R${newSalary}")

salaryIncrease()