from random import randint
from time import sleep
cores = {'vermelho':'\033[1;31m', 'verde':'\033[1;32m','azul':'\033[1;34m','limpa':'\033[m'}
opcoes = ['Papel', 'Pedra', 'Tesoura']
escolhaComputador = randint(0,2)
escolhaJogador = int(input('Escolhe entre: \n[0] - Papel\n[1] - Pedra\n[2] - Tesoura\n'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POOO!')
if escolhaComputador == 0: # Computador escolheu papel
    if escolhaJogador == 0:
        print(f'{cores["azul"]}{cores["azul"]}Empate!{cores["limpa"]}{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    elif escolhaJogador == 1:
        print(f'{cores["verde"]}{cores["vermelho"]}Você perdeu!{cores["limpa"]}{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    elif escolhaJogador == 2:
        print(f'{cores["vermelho"]}{cores["verde"]}Você venceu!{cores["limpa"]}{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    else:
        print(f'{cores["vermelho"]}Digite uma opção válida.{cores["limpa"]}')
if escolhaComputador == 1: #Computador escolheu Pedra
    if escolhaJogador == 0:
        print(f'{cores["verde"]}Você venceu!{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    elif escolhaJogador == 1:
        print(f'{cores["azul"]}Empate!{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    elif escolhaJogador == 2:
        print(f'{cores["vermelho"]}Você perdeu!{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    else:
        print(f'{cores["vermelho"]}Digite uma opção válida.{cores["limpa"]}')
if escolhaComputador == 2: #Computador escolheu Tesoura
    if escolhaJogador == 0:
        print(f'{cores["vermelho"]}Você perdeu!{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    elif escolhaJogador == 1:
        print(f'{cores["verde"]}Você venceu!{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    elif escolhaJogador == 2:
        print(f'{cores["azul"]}Empate!{cores["limpa"]} O computador escolheu {opcoes[escolhaComputador]}')
    else:
        print(f'{cores["vermelho"]}Digite uma opção válida.{cores["limpa"]}')
