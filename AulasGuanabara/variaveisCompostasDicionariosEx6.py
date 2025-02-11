listaJogadores = list()
while True:
    jogador = {'nome':str(input('Nome:')).capitalize(),
            'partidas':int(input('Quantidade de partidas: '))}
    temp = list()
    golsPartida = list()
    somaGols = 0
    for p in range(0, jogador['partidas']):
        gol = int(input(f'Quantos gols na partida {p+1}:'))
        somaGols += gol
        temp.append(gol)
        golsPartida.append(temp[:])
        temp.clear()
    jogador['golsPartida'] = golsPartida
    jogador['totalGols'] = somaGols
    listaJogadores.append(jogador.copy())
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('-='*20)
print('cod',end='')
for i in jogador.keys():
    print(f' {i:<15}',end='')
print()
print('-='*20)
for k, v in enumerate(listaJogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*20)
while True:
    print(listaJogadores)
    c = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    for c, j in enumerate(listaJogadores):
        for j in j['golsPartida']:
            print(c)
    if c == 999:
        break
print('Fim')