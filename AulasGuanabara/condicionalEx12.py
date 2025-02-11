from datetime import date
# Dicionário de cores
cores = {'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'limpa':'\033[m'}
sexo = str(input('Digite seu sexo. [M/F]')).upper().strip()
if sexo == 'M':
    anoNascimento = int(input('Digite o ano em que você nasceu:'))
    idade = date.today().year-anoNascimento
    if idade > 18:
        anosAtrasado = idade - 18
        print(f'{cores["vermelho"]}Seu tempo de alistamento já passou! Você está atrasado {anosAtrasado} ano(s){cores["limpa"]}. \nVocê devia ter se alistado em {anoNascimento + 18}.')
    elif idade == 18:
        print(f'{cores["verde"]}Você vai se alistar esse ano! Você tem {idade} anos.{cores["limpa"]}')
    else:
        anosRestantes = 18 - idade
        anoAlistamento = date.today().year + anosRestantes
        print(f'{cores["amarelo"]}Você vai se alistar em {anosRestantes} ano(s), no ano de {anoAlistamento}{cores["limpa"]}')
elif sexo == 'F':
    print(f'{cores["amarelo"]}Você é mulher, você não precisa se alistar.{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}Digite um opção válida.{cores["limpa"]}')