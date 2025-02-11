# Jogo adivinhação
from random import randint
escolhaComputador = randint(0,10)
escolhaJogador = 0
contador = 0
while escolhaComputador != escolhaJogador:
    escolhaJogador = int(input('Escolha um número entre 0 e 10: '))
    if escolhaJogador > escolhaComputador:
        print('\033[1;31mMenos - Você errou! Tente novamente.\033[m')
        contador = contador + 1
    elif escolhaJogador < escolhaComputador:
        print('\033[1;31mMais - Você errou! Tente novamente.\033[m')
        contador += 1
print(f'\033[1;32mVocê acertou!\033[m O computador escolheu {escolhaComputador}\nForam necessárias {contador} tentativas') 