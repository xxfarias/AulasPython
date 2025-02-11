lista = [[], []]
for c in range (1, 8):
    num = int(input(f'Digite o número {c}: '))
    if num % 2 == 0:
        lista[0].insert(1, num)
    else:
        lista[1].insert(0, num)
lista[0].sort()
lista[1].sort()
print(f'Os pares são: {lista[1]}')
print(f'Os ímpares são: {lista[0]}')