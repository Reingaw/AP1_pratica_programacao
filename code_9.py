isOver = 0
count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def paymentList(sale):
    salary = 200 + (sale * (9 / 100))
    for i in range(2,11):
        if (i * 100) < salary < ((i * 100) + 99) and salary < 1000:
            count[i - 2] += 1
        elif salary >= 1000:
            count[i - 2] += 1

while not isOver:
    sale = float(input("Digite 0 para sair ou \n"
                       "Digite o valor da venda: ").replace(",", ""))
    if sale != 0:
        paymentList(sale)
    else:
        isOver = 1
        print('Quantidade de vendedores que receberam entre \n'
              f'R$200 - R$299: {count[0]} \n'
              f'R$300 - R$399: {count[1]} \n'
              f'R$400 - R$499: {count[2]} \n'
              f'R$500 - R$599: {count[3]} \n'
              f'R$600 - R$699: {count[4]} \n'
              f'R$700 - R$799: {count[5]} \n'
              f'R$800 - R$899: {count[6]} \n'
              f'R$900 - R$999: {count[7]} \n'
              f'R$1000 ou mais: {count[8]} ')