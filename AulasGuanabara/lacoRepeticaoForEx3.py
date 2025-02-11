# Soma de números impares divisiveis por 3 entre 0 e 500
soma = 0
contador = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        contador = contador + 1
        print(c, end=' ')
print(f'A soma total de {contador} foi de: {soma}')