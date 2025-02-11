# Soma somente de números pares
from time import sleep
print('Soma somente de números pares, digite 6 números inteiros')
soma = 0
for c in range (1,7):
    num = int(input('Digite o valor para soma: '))
    if (num % 2 == 0):
        soma = soma + num
        sleep(0.5)
        print(f'Contador: {c}. A soma é de {soma} \n')
    else:
        print(f'Você digitou um número ímpar, contador: {c}. Ele não será adicionado na soma, a soma está em: {soma}\n')
        sleep(0.5)
sleep(0.5)
print(f'A soma total foi de {soma}\n--- FIM ---')