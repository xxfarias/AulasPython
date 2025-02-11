peso = float(input(f'Digite o peso da pessoa 1:'))
maiorPeso = peso
menorPeso = peso
for c in range(0,6):
    peso = float(input(f'Digite o peso da pessoa {c}:'))
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso
print(f'O maior peso foi de {maiorPeso}\nO menor peso foi de {menorPeso}')