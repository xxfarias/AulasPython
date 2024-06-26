import math
num1 = float(input('Entre com um angulo: '))
seno = math.sin(math.radians(num1))
cosseno = math.cos(math.radians(num1))
tg = math.tan(math.radians(num1))
print('O angulo {} tem o seno {}, o cosseno {} e a tangente {}'.format(num1, seno, cosseno, tg))