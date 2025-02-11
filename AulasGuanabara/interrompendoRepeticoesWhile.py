num = contador = somador = maiorValor = menorValor = 0
while True:
    num = int(input('Digite 999 para parar\nDigite um número para a soma: '))
    if num == 999:
        break
    if contador == 0:
        menorValor = maiorValor = num
    else:
        if num > maiorValor:
            maiorValor = num
        if num < menorValor:
            menorValor = num
    somador += num
    contador += 1
print(f'Foram digitados {contador} números e a soma foi {somador}.\nO maior valor digitado foi {maiorValor} e o menor foi {menorValor}')