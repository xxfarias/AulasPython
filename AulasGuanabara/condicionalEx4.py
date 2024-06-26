distancia = float(input('Qual a distância percorrida em km? '))
if distancia > 200:
    precoPassagem = distancia * 0.45
    print(f'O preço da passagem é R${precoPassagem}')
else:
    precoPassagem = distancia * 0.5
    print(f'O preço da passagem é R${precoPassagem}')
print('---FIM---')