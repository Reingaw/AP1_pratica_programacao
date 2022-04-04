def multiplicationTable():
    factor = int(input("Digite um numero: "))
    i = 1
    while i <= 10:
        result = factor * i
        print(f"{factor} x {i} = {result}")
        i += 1

multiplicationTable()