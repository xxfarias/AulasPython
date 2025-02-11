# Sequencia de Fibonacci
numero = int(input('Digite a quantidade de números para a sequência de Fibonacci: '))
print('=-'*10,'Sequência de Fibonacci','-='*10)
contador = 3
# Contador começando no 3 porque já foram exibidos dois números da sequência
fibonacci = 1
fibonacci2 = 1
fibonacci3 = 0
if numero == 1:
    print(f'{fibonacci}→',end='')
elif numero == 2:
    print(f'{fibonacci}→{fibonacci2}→',end='')
else:
    print(f'{fibonacci}→{fibonacci2}→',end='')
while contador <= numero:
    fibonacci3 = fibonacci + fibonacci2
    print(f'{fibonacci3}→',end='')
    fibonacci = fibonacci2
    fibonacci2 = fibonacci3
    contador = contador + 1
print('Fim') 