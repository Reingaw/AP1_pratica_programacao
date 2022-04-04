def idealWeight():
    hText = input('Digite sua altura: ')
    h = float(hText.replace(",", "."))
    gender = input('Digite seu Sexo (M | F): ')

    if(gender.upper() == 'M'):
        result = (72.7 * h) - 58
    else:
        result = (62.1 * h) - 44.7
    ideal = round(result)
    print(f"Seu peso ideal é {ideal}Kg")

idealWeight()