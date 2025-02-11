from time import sleep
notas = list()
temp = list()
temp2 = list()
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
    temp.append(nome)
    nota1 = float(input('Digite a primeira nota: '))
    temp2.append(nota1)
    nota2 = float(input('Digite a segunda nota: '))
    temp2.append(nota2)
    media = (nota1 + nota2) / 2
    temp2.append(media)
    temp.append(temp2[:])
    notas.append(temp[:])
    temp2.clear()
    temp.clear()
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'{'Nº':<10}{'Nome':^10}{'Média':>10}')
for c in range(0, len(notas)):
    print(f'{c:<10}{notas[c][0]:^10}{notas[c][1][2]:>10}')
print('-='*20)
while True:
    aluno = ' '
    aluno = int(input('Mostar nota de qual aluno? [999 para interromper] '))     
    if aluno == 999:
        break
    print(f'As notas de {notas[aluno][0]} são: {notas[aluno][1][0:2]}')
print('Finalizando...')
sleep(0.3)  
print('Volte sempre!') 