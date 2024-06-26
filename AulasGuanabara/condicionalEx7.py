cores = {'limpa':'\033[m', 
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}
salario = float(input('Digite seu salário: '))
if salario > 1250:
    novoSalario = salario + (salario * 0.1)
    print(f'Seu novo salário é de {cores['verde']}R${novoSalario}{cores['limpa']}')
else:
    novoSalario = salario + (salario * 0.15)
    print(f'Seu novo salário é de {cores['vermelho']}R${novoSalario}{cores["limpa"]}')
print('---FIM---')