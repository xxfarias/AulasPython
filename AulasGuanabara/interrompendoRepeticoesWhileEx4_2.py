contadorMaiorIdade = contadorHomem = contadorMulherVinte = 0
while True:
    sexo = ''
    escolha = ' '
    print('-'*30)
    print('CADASTRE UMA PESSOA:')
    print('-'*30)
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    print('\033[1;32mCadastro realizado\033[m')
    if idade > 18:
        contadorMaiorIdade +=1
    if sexo == 'M':
        contadorHomem += 1
    if sexo == 'F' and idade < 20:
        contadorMulherVinte += 1
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
       break
print(f'Foram cadastradas {contadorMaiorIdade} pessoas com mais de 18 anos;\nForam cadastrados {contadorHomem} homens;\nForam cadastradas {contadorMulherVinte} mulheres abaixo dos 20 anos.')