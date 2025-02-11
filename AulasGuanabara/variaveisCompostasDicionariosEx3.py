from datetime import date
dados = {'nome':str(input('Nome:')).capitalize().strip()}
anoNascimento = int(input('Digite seu ano de nascimento:'))
dados['idade'] = date.today().year - anoNascimento
dados['carteira'] = int(input('Carteira de trabalho [0 se não possuir]: '))
if dados['carteira'] == 0:
    print('-='*20)
    for k, v in dados.items():
        print(f'{k}:{v}')
else:
    dados['anoContratacao'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] =  (dados['anoContratacao'] + 35) - anoNascimento
    dados['salario'] = float(input('Digite seu salário: R$')) 
    print('-='*20)
    for k,v in dados.items():
        print(f'{k}:{v}')
    