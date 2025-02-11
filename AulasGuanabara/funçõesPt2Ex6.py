from time import sleep

c = ('\033[m',       # 0 - Sem cores
    '\033[0;31m',    # 1 - Vermelho
    '\033[0;32m',    # 2 - Verde
    '\033[0;33m',    # 3 - Amarelo
    '\033[0;34m'     # 4 - Azul
    );

def titulo(msg, cor=0):
    tamanho = int(len(msg)) + 4
    print(c[cor], end='')
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)
    print(c[0], end='')
    sleep(0.3)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[3])
    help(com)
    print(c[0], end='')
    sleep(0.5)

while True:
    titulo('Sistema de ajuda PyHelp',1)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
       break
    else:
       ajuda(comando)
titulo('Até logo!', 2)
