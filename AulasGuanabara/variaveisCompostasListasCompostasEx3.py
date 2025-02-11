# Matriz
matriz = [[], [] , [], [], [], [] , [], [], []]
somaPares = somaTerceiraColuna = 0
for c in range (0, 9):
    num = int(input(f'Digite o valor ({c}): '))
    if num % 2 == 0:
        somaPares += num
    if c == 2 or c == 5 or c ==8:
        somaTerceiraColuna += num
    if 2<c<6:
        if c == 3:
            maiorValor = menorValor = num
        else:
            if num > maiorValor:
                maiorValor = num
            if num< menorValor:
                menorValor = num
    matriz[c].append(num)
for c in range (0, 3):
    print(matriz[c], end='')
print()
for c in range (3, 6):
    print(matriz[c], end='')
print()
for c in range (6, 9):
    print(matriz[c], end='')
print()
print('-'*30)
print(f'A soma dos pares foi de {somaPares}')
print(f'A soma da terceira coluna é de {somaTerceiraColuna}')
print(f'O maior valor da linha é {maiorValor} e o menor é {menorValor}')
