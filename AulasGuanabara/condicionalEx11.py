# Dicionário de cores
cores = {'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'limpa':'\033[m'}
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print(f'{cores["verde"]}O primeiro número ({num1}) é o MAIOR!{cores["limpa"]}')
elif num1 == num2:
    print(f'{cores["amarelo"]}Os numeros {num1} e {num2} são iguais.{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}O segundo número ({num2}) é o MAIOR!{cores["limpa"]}')