from time import sleep
pessoas = []
dados = []
contador = 0
while True:
    contador += 1
    nome = input(f'Digite o nome da pesssoa {contador}: ')
    dados.append(nome)
    peso = (float(input(f'Digite o peso da pessoa {contador}: ')))
    dados.append(peso)
    if contador == 1:
        maiorPeso = menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso
    sleep(0.2)
    pessoas.append(dados[:])
    print(f'\033[32;1mPessoa {contador} adicionada com sucesso\033[m')
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break  
print('=-'*35)
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pesssoas')
print(f'O mais pesados foram: ',end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'{p[0]} com {maiorPeso}Kg')
print(f'Os mais leves foram: ',end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'{p[0]} com {menorPeso}Kg')