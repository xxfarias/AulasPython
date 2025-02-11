def ficha(nome="<desconhecido>", gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')
nomeJog = str(input('Nome: ')).capitalize()
totGols = str(input('Gols: '))
if totGols.isnumeric():
    totGols = int(totGols)
else:
    totGols = 0
if nomeJog.strip() == '':
    ficha(gols = totGols)
else:
    ficha(nomeJog, totGols)
