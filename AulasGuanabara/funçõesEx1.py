# Area
def titulo(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)
titulo('Calculadora de terreno')
def area (largura, altura):
    a = largura * altura
    print(f'A área de um terreno de {largura}m *{altura}m é de {a}m²')
largura = float(input('Digite a largura em m: '))
altura = float(input('Digite a altura em m: '))
area(largura, altura)