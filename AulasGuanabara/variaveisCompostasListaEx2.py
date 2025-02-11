lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('\033[31;1mEsse valor já foi digitado. Não foi adicionado a lista!\033[m')
    else:
        lista.append(num)
        print('\033[1;32mValor adicionado!\033[m')
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
            break
print(f'A lista ficou como:{lista}')
print(f'Lista em ordem: {sorted(lista)}')
print(f'O maior valor digitado foi o {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')
