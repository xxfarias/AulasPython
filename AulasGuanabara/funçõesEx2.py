def escreva(msg):
    tamanhoA = len(msg) + 4
    print('~'*tamanhoA)
    print(f'{msg:^{tamanhoA}}')
    print('~'*tamanhoA)
escreva('Joao')
escreva('SOCIEDADE ESPORTIVA PALMEIRAS')
escreva('Guilherme Farias de Oliveira')