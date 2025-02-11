lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    print('\033[32;1mValor adicionado.\033[m')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\033[35;1mQuer continuar? [S/N]\033[m')).strip().upper()[0]
    if continuar == 'N':
        break
listaPares = []
listaImpares = []
for c in lista:
    if c % 2 == 0:
        listaPares.append(c)
    else:
        listaImpares.append(c)
print(f'Lista final: {lista}')
print(f'Lista de pares: {listaPares}')
print(f'Lista de impares: {listaImpares}')