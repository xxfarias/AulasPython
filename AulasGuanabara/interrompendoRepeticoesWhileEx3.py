# Par ou ímpar
from random import randint
vitorias = 0
while True:
    print('='*50,'\nPAR OU IMPAR\n',end='')
    print('='* 50)
    escolhaJogador = ' '
    while escolhaJogador not in "PI":
        escolhaJogador = (input('Impar ou par: ')).strip().upper()[0]
    if escolhaJogador == 'I':
        escolhaJogador = 'Impar'
    else:
        escolhaJogador = 'Par'
    numComputador = randint(0,10)
    numJogador = int(input('Digite um número: '))
    soma = numComputador + numJogador
    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    if resultado == escolhaJogador:
        print(f'\033[1;32mVocê ganhou!\033[m\nO computador escolheu {numComputador}, a soma foi de {soma} e o resultado foi {resultado}')
        vitorias += 1
        print(f'As vitórias estão em: {vitorias}')
    else:
        print(f'\033[1;31mVocê perdeu!\033[m\nO computador escolheu {numComputador}, a soma foi de {soma} e o resultado foi {resultado}')
        break
print(f'Você venceu {vitorias} vezes')