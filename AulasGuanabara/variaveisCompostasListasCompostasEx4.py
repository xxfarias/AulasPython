# Mega Sena
from random import randint
from time import sleep
lista = list()
temp = list()
print('-'*30)
print(f'{'GERADOR DE MEGA SENA':^30}')
print('-'*30)
quantidadeJogos = int(input('Quer gerar quantos jogos? '))
print(f'Sorteando {quantidadeJogos} jogos')
for c in range (0, quantidadeJogos):
    for cont in range(0,6):
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
    lista.append(temp[:])
    temp.clear()
    sleep(0.2)
    lista[c].sort()
    print(f'Jogo {c+1}: {lista[c]}')
