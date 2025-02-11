lista = []
contador = 0
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    print('Valor adicionado')
    contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Lista final: {lista}, foram digitados {contador} valores, o tamanho da lista é {len(lista)}')
print(f'Lista de forma decrescente {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O número 5 foi digitado na posição {lista.index(5)}')
else:
    print(f'O número 5 não foi digitado')