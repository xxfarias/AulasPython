from datetime import date
menorIdade = 0
maiorIdade = 0
for c in range (1, 8):
    anoNascimento = int(input(f'Digite o ano de nascimento da pessoa {c}: '))
    idade = date.today().year - anoNascimento
    if idade >= 21:
            maiorIdade = maiorIdade + 1
            print(f'A pessoa {c} tem {idade} anos')
    elif idade <21:
            menorIdade = menorIdade + 1
            print(f'A pessoa {c} tem {idade} anos')
print(f'São {maiorIdade} pessoas maiores de idade e {menorIdade} pessoas menores da idade')