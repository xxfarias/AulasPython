# Fatorial
from math import factorial
c = int(input('Digite um número para a fatorial: '))
prova = factorial(c)
resultado = c
print(f'{c}! = ', end='')
if c != 0:
    for c in range(c,0,-1):
        if c != 1:
            print(f'{c}*',end='')
            c -= 1
            resultado = resultado * c
        else:
            print(f'{c} = ',end='')
    print(resultado)
else:
    print(1)
print(prova)