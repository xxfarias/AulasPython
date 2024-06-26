# Dicionário de cores
cores = {'verde':'\033[1;32m', 'vermelho':'\033[1;31m', 'limpa':'\033[m'}
num = int(input('Digite um número inteiro: '))
base = int(input('''Escolha a base de conversão:
"1" - Para binário
"2" - Para hexadecimal
"3" - Para octal
'''))
if base == 1:
    numBin = bin(num)
    print(f'Conversão para binário: {cores["verde"]}{numBin}{cores["limpa"]}')
elif base == 2:
    numHex = hex(num)
    print(f'Conversão para hexadecimal: {cores["verde"]}{numHex}{cores["limpa"]}')
elif base == 3:
    numOct = oct(num)
    print(f'Conversão para base octal: {cores["verde"]}{numOct}{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}Opção inválida.{cores["limpa"]}')