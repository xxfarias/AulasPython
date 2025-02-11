# Numero primo
cores = {'vermelho':'\033[1;31m', 'verde':'\033[1;32m','azul':'\033[1;34m','limpa':'\033[m'}
num = int(input('Insira um número: '))
soma = 0
for c in range (1, num+1):
    if num % c == 0:
        print(f'{num} é divisivel por {cores["vermelho"]}{c}{cores["limpa"]}')
        soma = soma + 1
    else:
        print(f'{num} não é divisel por {c}')
        soma = soma + 0
if soma == 2:
    print(f'O numero {num} é primo, foi divido {soma} vezes')
else:
    print(f'O numero {num} não é primo, foi divido {soma} vezes')