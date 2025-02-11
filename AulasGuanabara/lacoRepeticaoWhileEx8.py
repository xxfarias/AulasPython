cores = {'verde':'\033[1;32m', 'limpa':'\033[m'}
pergunta = ''
num = somador = contador = 0
maiorValor = menorValor = num
while pergunta != 'N':
    num = int(input('Digite um número: '))
    if contador == 0:
        maiorValor = menorValor = num
    else:
        if  num > maiorValor:
            maiorValor = num
        if num < menorValor:
            menorValor = num
    somador = somador + num
    contador += 1
    pergunta = str(input(f'{cores["verde"]}Quer continuar? [S/N]{cores["limpa"]}')).strip().upper()[0]
media = somador / contador
print(f'A média foi de {media:.2f}\nO maior valor digitado foi {maiorValor} e o menor foi {menorValor}')
print('Fim')  