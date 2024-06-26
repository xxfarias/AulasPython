cores = {'vermelho':'\033[1;31m',
         'azul':'\033[1;34m',
         'limpa':'\033[m'}
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if (num1 > num2 and num1 > num3):
    print(f'O maior número é o {cores["vermelho"]}{num1}{cores["limpa"]}!')
elif (num2 > num1 and num2 > num3):
        print(f'O maior número é o {cores["vermelho"]}{num2}{cores["limpa"]}!')
else:
    print(f'O maior número é o {cores["vermelho"]}{num3}{cores["limpa"]}!')
if (num1 < num2 and num1 < num3):
    print(f'O menor valor é o {cores["azul"]}{num1}{cores["limpa"]}!')
elif (num2 < num1 and num2 < num3):
    print(f'O menor número é o {cores["azul"]}{num2}{cores["limpa"]}!')
else:
    print(f'O menor número é o {cores["azul"]}{num3}{cores["limpa"]}!')