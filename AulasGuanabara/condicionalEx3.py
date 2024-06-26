num = float(input('Digite um número: '))
restoDivisao = (num % 2)
print(f'O resto da divisão é: {restoDivisao}')
if (restoDivisao == 0):
    print('É par!')
else:
    print('É impar!')