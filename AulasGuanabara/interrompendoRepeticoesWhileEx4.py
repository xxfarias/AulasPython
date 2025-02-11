contadorMulherVinte = contadorHomem = contadorMaiorIdade = 0
while True:
    escolha = str(input('Começar o cadastro? [S/N]')).strip().upper()
    if escolha == 'S':
        idade = int(input('Digite sua idade: '))
        sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()
        if idade > 18:
            contadorMaiorIdade += 1
        if sexo == 'M':
            contadorHomem += 1
        if sexo == 'F' and idade < 20:
            contadorMulherVinte += 1
    else:
        break
    print('\033[1;32mCadastro realizado\033[m\n',end='')
    print('='*30)
print(f'São {contadorMaiorIdade} pessoas com mais de 18 anos\nForam cadastrados {contadorHomem} homens\nForam cadastradas {contadorMulherVinte} mulheres com menos de 20 anos.')