from datetime import date
# Dicionário de cores
cores = {'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'limpa':'\033[m'}
anoNascimento = int(input('Digite o ano em que você nasceu:'))
idade = date.today().year-anoNascimento
if idade > 18:
    anosAtrasado = idade - 18
    print(f'{cores["vermelho"]}Seu tempo de alistamento já passou!. Você está atrasado {anosAtrasado} ano(s){cores["limpa"]}')
elif idade == 18:
    print(f'{cores["verde"]}Você vai se alistar esse ano! Você tem {idade} anos.{cores["limpa"]}')
else:
    anosRestantes = 18 - idade
    anoAlistamento = date.today().year + anosRestantes
    print(f'{cores["amarelo"]}Você vai se alistar em {anosRestantes} ano(s), no ano de {anoAlistamento}{cores["limpa"]}')