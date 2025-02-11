def titulo(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)
titulo('Funções')
def soma(a, b):
    s = a+b
    print(f'{a} + {b} = {s}')
soma(4, 5)
titulo('Desempacotar')
def contador(*num):
    for valor in num:
        valor+=1
    print(valor)
contador(1, 23,3,12)
valores = [2 ,21, 312, 3, 4, 0]
print('-'*20)
def dobra(a):
    print(a)
    cont = 0
    while cont < len(a):
        print(f'{a[cont] * 2} ', end='')
        cont += 1
dobra(valores)
