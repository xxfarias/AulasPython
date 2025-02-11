campeonatoBrasileiro = ('Botafogo','Palmeiras','Flamengo','São Paulo','Bahia',
                        'Cruzeiro','Fortaleza','Athletico-PR','Vasco','Bragantino',
                        'Atlético-MG','Juventude','Internacional','Criciúma','Cuiabá',
                        'Vitória','Corinthians','Grêmio','Atlético-GO','Fluminense')
print(f'Os cinco primieiros colocados são: {campeonatoBrasileiro[:5]}')
contador = 0
for contador in range(0,5):
    print(f'Posição {contador+1}:{campeonatoBrasileiro[contador]}')
print(f'Os quatro ultimos colocados são {campeonatoBrasileiro[-4:]}')
for contador in range(16,len(campeonatoBrasileiro)):
    print(f'Os ultimos 4 colocados são: {campeonatoBrasileiro[contador]}')
print(f'Ordem alfábetica do Brasileirão {sorted(campeonatoBrasileiro)}')
print(f'O vasco está na posição: {campeonatoBrasileiro.index('Vasco')+1}')
while True:
    posicao = int(input('Digite a posição para descobrir o time: '))
    posicao -= 1
    if 0<=posicao<=20:
        break
    print('\033[1;31mPosição inválida. Digite um número entre 1 e 20.\033[m')
print(campeonatoBrasileiro[posicao])
while True:
    time = str(input('Digite o nome do time para achar sua posição: ')).capitalize().strip()
    if time in campeonatoBrasileiro:
        break
print(f'{campeonatoBrasileiro.index(time)+1}º')    