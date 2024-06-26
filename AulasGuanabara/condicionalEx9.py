# Dicionário de cores
cores = {'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'limpa':'\033[m'}
# Aprovar empréstimo 
valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos você irá pagar: '))
prestacaoAnualCasa = valorCasa / anos
prestacaoMensalCasa = prestacaoAnualCasa / 12
salarioDividido = salario * 0.3
if prestacaoMensalCasa > salarioDividido:
    print(f'{cores["vermelho"]}EMPRESTIMO NEGADO!!!{cores["limpa"]} Você não pode financiar essa casa, a prestação mensal de R${prestacaoMensalCasa:.2f} é maior que os 30% do seu salário de R${salario}, que é {cores["amarelo"]}R${salarioDividido:.2f}{cores["limpa"]}')
else:
    print(f'{cores["verde"]}EMPRÉSTIMO APROVADO!!!{cores["limpa"]} Você pode financiar a casa, a prestação mensal é de R${prestacaoMensalCasa:.2f} e não execede 30% do seu salário, que corresponde a {cores["amarelo"]}R${salarioDividido:.2f}{cores["limpa"]}')
print('---FIM---')