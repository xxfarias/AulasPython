from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores: ',end='')
    for cont in range(0, 5):
        n = randint(1,10)
        print(f'{n} ' , end='', flush=True)
        sleep(0.15)
        lista.append(n)
    print()
def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares da lista {lista} foi de {soma}')            
numeros = list()
sorteia(numeros)
somaPar(numeros)