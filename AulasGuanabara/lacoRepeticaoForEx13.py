num = int(input("Digite um número para a fatorial: "))
print(f'{num}! = ',end='')
resultado = 1
for c in range (num, 0, -1):
    if c != 1:
        print(f'{c}*', end='')
        resultado = resultado * c
    else:
        print(f'{c}=',end='')
print(f' {resultado}')