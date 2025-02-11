from time import sleep
aluno = dict()
turma = list()
while True:
    aluno['nome'] = str(input('Nome: ')).capitalize()
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        aluno['situação'] = '\033[32;1maprovado\033[m'
    elif 5 <= aluno['media'] < 7:
        aluno['situação'] = '\033[33;1mrecuperação\033[m'
    else:
        aluno['situação'] = '\033[31;1mreprovado\033[m'
    turma.append(aluno.copy())
    print('\033[32;1mAluno cadastrado!\033[m')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
for a in turma:
    for k, v in a.items():
        print(f'{k}: {v}')
    print()
sleep(0.5)
print('\033[31;1mPrograma finalizado\033[m')