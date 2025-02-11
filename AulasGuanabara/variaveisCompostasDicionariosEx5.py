listaPessoas = list()
pessoa = dict()
c = somaIdade = media = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize().strip()
    sexo = ' '
    while sexo not in "FM":
        sexo = str(input('Sexo: [F/M]')).upper().strip()[0]
        if sexo not in "FM":
            print('\033[31;1mERRO! Por favor, digite apenas M ou F.\033[m')    
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    # Soma de idades para a média
    somaIdade += pessoa['idade']
    # Contador de pessoas
    c += 1
    print(f'\033[32;1mPessoa {c} cadastrada!\033[m')
    listaPessoas.append(pessoa.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar not in 'SN':
            print('\033[31;1mERRO! Digite apenas S ou N.\033[m ')    
    if continuar == 'N':
        break
print(listaPessoas)
print('=-'*30)
media = somaIdade / c
print(f'Foram cadastradas {c} pessoas')
print(f'Média de idade: {media:.2f} anos')
#Lista mulheres/ 
print(f'Lista de mulheres: ')
for p in listaPessoas:
    if p['sexo'] in 'F':
        print(f'{p['nome']}')
print('Pessoas com idade acima da média: ')
for p in listaPessoas:
    if p['idade'] > media:
        print(f'{p['nome']} com {p['idade']} anos')