cores = {'ciano':'\033[1;36m',
         'roxo':'\033[1;35m',
         'limpa':'\033[m'}
ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0):
    print(f'O ano {ano} {cores["ciano"]}É BISSEXTO{cores["limpa"]}!!!')
else:
    print(f'O ano {ano} não é {cores["roxo"]}bissexto{cores["limpa"]}!')
print('---FIM---')