def calculateNetSalary():
    salaryByHour = float(input("Digite o valor da sua hora: ").replace(",", "."))
    hoursWorked = float(input("Digte a quantidade de horas trabalhadas: ").replace(",", "."))
    grossSalary = salaryByHour * hoursWorked
    incomeTax = round(grossSalary * (11/100), 2)
    inss = round(grossSalary * (8/100), 2)
    union = round(grossSalary * (5/100), 2)
    netSalary = grossSalary - (incomeTax + inss + union)
    print(f"Salario Bruto: R$ {grossSalary}")
    print(f"IR(11%): R$ {incomeTax}")
    print(f"INSS(8%): R$ {inss}")
    print(f"Sindicato(5%): R$ {union}")
    print(f"Salario Líquido: R$ {netSalary}")

calculateNetSalary()