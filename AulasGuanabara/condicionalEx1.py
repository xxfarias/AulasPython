from random import randint
from time import sleep
num = randint(1,5)
num1 = int(input('Escolhi um número de 1 a 5, tente adivinhar qual foi: '))
print('ANALISANDO...')
sleep(2)
if num == num1:
    print('Você acertou, eu escolhi o número {}'.format(num))
else:
    print('Você errou, eu escolhi o número {}'.format(num))
print('---FIM---')