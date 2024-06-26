# Dicionário de cores
cores = {'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'limpa':'\033[m'}
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'{cores["verde"]}APROVADO!{cores["limpa"]} Sua média foi de {media:.2f}')
elif media >= 5.0 and media <= 6.9:
    print(f'{cores["amarelo"]}RECUPERAÇÃO!{cores["limpa"]} Sua média foi de {media:.2f}')
else:
    print(f'{cores["vermelho"]}REPROVADO!{cores["limpa"]} Sua média foi de {media:.2f}')