somador = contador = 0
while True:
    num = int(input('Digite 999 para parar\nDigite um número inteiro: '))
    if num == 999:
        break
    somador += num
    contador += 1
print(f'Foram digitados {contador} números e a soma deles é de {somador}')