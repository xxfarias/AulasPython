jogador = {'nome':str(input('Nome:')).capitalize(),
           'partidas':int(input('Quantidade de partidas: ')),          
           }
golsPartida = list()
somaGols = 0
for p in range(0, jogador['partidas']):
    gol = int(input(f'Quantos gols na partida {p+1}:'))
    somaGols += gol
    golsPartida.append(gol)
jogador['golsPartida'] = golsPartida
jogador['totalGols'] = somaGols
print('-='*20)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas:')
for c, gol in enumerate(jogador['golsPartida']):
    print(f'    Na partida {c+1}: {gol} gols')
print(f'Total de gols: {jogador["totalGols"]}')