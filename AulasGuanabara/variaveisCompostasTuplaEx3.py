from random import randint
listaNum = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
for c in listaNum:
    print(f'{c} ',end='')
print(f'\nLista ordenada: {sorted(listaNum)}')
print(f'O menor valor da lista é {sorted(listaNum)[0]}, o maior valor da lista é {sorted(listaNum)[-1]}')
print('-='*20)
# Usando MAX e MIN
print(f'O maior valor sorteado foi o {max(listaNum)} e o menor {min(listaNum)}')