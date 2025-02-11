# Leitura de sexo
sexo = ''
while sexo != "F" and sexo != 'M':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('\033[1;31mVocê digitou incorretamente! Digite novamente.\033[m\n')
if sexo == 'F':
    print('\033[1;32mSexo feminino registrado com sucesso!\033[m')
else:
    print('\033[1;32mSexo masculino registrado com sucesso!\033[m')