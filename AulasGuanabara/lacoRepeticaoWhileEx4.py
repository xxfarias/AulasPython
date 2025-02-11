# Fatorial 
num = int(input('Digite um número para a fatorial: '))
print(f'{num}! = ',end='')
resultado = num
while num >= 1:
    if num != 1:
        print(f'{num}*',end='')
        num -= 1
        resultado = resultado * num
    else:
        print(f'{num} = ',end='')
        num -= 1
print(f'{resultado}\nFim')

