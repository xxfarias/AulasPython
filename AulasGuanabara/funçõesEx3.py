from time import sleep
def contador(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c = abs(c)
    print(f'Contagem de {a} até {b} de {c} em {c}: ')
    if a > b and c > 0:
        c = -c
    if a > b:
        for cont in range(a, b-1, c):
            print(f'{cont} ' , end='', flush=True)
            sleep(0.15) 
        print('Fim!')
        print('-='*25)
    elif b > a:
        for cont in range(a, b+1, c):
           print(f'{cont} ' , end='', flush=True)
           sleep(0.15) 
        print('Fim!')
        print('-='*25) 
contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada: ')
num1 = int(input('Inicio: '))
num2 = int(input('Fim: '))
num3 = int(input('Passo: '))
contador(num1, num2, num3)