from random import randint
from time import sleep
from operator import itemgetter
resultados = {'jogador1' : randint(1, 6), 'jogador2' : randint(1, 6),
              'jogador3' : randint(1, 6), 'jogador4' : randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
for k, v in resultados.items():
    print(f'    {k}: {v}')
    sleep(0.5)
print('-'*30)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('Ranking: ')
for c, v in enumerate(ranking):
    print(f'    {c+1}º lugar:{v[0]}:{v[1]}')
    sleep(0.1)
