isOver = 0

def paymentValue(quota, days):
    if days == 0:
        printQuota(quota)
    else:
        nQuota = round(quota + (quota * (0.001 / 100)) + (quota * (3 / 100)), 2)
        printQuota(nQuota)

def printQuota(nQuota):
    print(f"Valor da parcela: {nQuota}")

while not isOver:
    quota = float(input("Digite o valor da parcela ").replace(",", ""))
    days = float(input("Digite os dias de atraso ").replace(",", ""))

    if quota != 0:
        paymentValue(quota, days)
    else:
        isOver = 1