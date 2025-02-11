from time import sleep
while True:
    contador = resultado = 0
    num = int(input('Digite um número para gerar a tabuada: '))
    print('-'*20)
    if num < 0:
        break
    while contador < 10:
        contador += 1
        resultado = num * contador
        print(f'{num} * {contador} = {resultado}')  
    print('-'*20)
sleep(0.5)
print('PROGRAMA TABUADA ENCERRADO.')