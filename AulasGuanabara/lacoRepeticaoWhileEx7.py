contador = somador = numero = 0
while numero != 999:
    numero = int(input('Digite 999 para parar o programa.\nDigite um número: '))
    if numero != 999:
        somador = somador + numero
        contador += 1
print(f'Fim\nA soma de todos os números {contador} digitados foi de: {somador}')