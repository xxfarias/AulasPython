numeros = []
temp = []
for c in range (1,8):
    num = int(input(f'Digite o número {c}: '))
    if num % 2 == 0:
        temp.insert(0, num)
    else:
        temp.insert(-1, num)
    numeros.append(temp[:])
    temp.clear()
numeros.sort()
print(numeros)
print(f'Os números pares são: ',end='')
for numero in numeros:
    if numero[0] % 2 == 0:
        print(f'{numero[0]} ',end='')
print()
print(f'Os números impares são: ',end='')
for numero in numeros:
    if numero[0] % 2 != 0:
        print(f'{numero[0]} ',end='')
