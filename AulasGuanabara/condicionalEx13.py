# Dicionário de cores
cores = {'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'limpa':'\033[m'}
print('Calculadora de média, digite suas notas entre 0 e 10:')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if 10>= media >= 7.0:
    print(f'{cores["verde"]}APROVADO!{cores["limpa"]} Sua média foi de {media:.1f}')
elif media >= 5.0 and media <= 6.9:
    print(f'{cores["amarelo"]}RECUPERAÇÃO!{cores["limpa"]} Sua média foi de {media:.1f}')
elif 0<= media < 5:
    print(f'{cores["vermelho"]}REPROVADO!{cores["limpa"]} Sua média foi de {media:.1f}')
else:
    print(f'{cores["vermelho"]}O calculo está errado! Sua média foi de {media}.{cores["limpa"]}')