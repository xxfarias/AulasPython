from datetime import date
#Dicionário de cores
cores = {'azul':'\033[1;33m', 'amarelo':'\033[1;34m', 'verde':'\033[1;32m', 'vermelho':'\033[1;31m', 'ciano':'\033[1;36m','limpa':'\033[m'}
anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - anoNascimento
if idade <= 9:
    print(f'{cores["amarelo"]}MIRIM{cores["limpa"]} - Você tem {idade} anos')  
elif idade>= 10 and idade<=14:
    print(f'{cores["azul"]}INFANTIL{cores["limpa"]} - Você tem {idade} anos')
elif idade > 14 and idade<20:
    print(f'{cores["verde"]}JUNIOR{cores["limpa"]} - Você tem {idade} anos')
elif idade>=20 and idade<21:
    print(f'{cores["vermelho"]}SÊNIOR{cores["limpa"]} - Você tem {idade} anos')
else:
    print(f'{cores["ciano"]}MASTER{cores["limpa"]} - Você tem {idade} anos')