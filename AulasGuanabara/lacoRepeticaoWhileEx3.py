from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 8:
    print(''' =-=-=MENU=-=-=
Digite:
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    [5] - Maior
    [6] - Menor
    [7] - Novos números
    [8] - Sair do programa
          ''')
    opcao = int(input('Digite a opção: '))
    sleep(0.5)
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif opcao == 3:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif opcao == 4:
        print(f'{num1} / {num2} = {num1/num2}')
    elif opcao == 5:
        if num1 > num2:
            print(f'O maior é o número {num1}')
        else:
            print(f'O maior número é o {num2}')
    elif opcao == 6:
        if num1 < num2:
            print(f'O menor número é o {num1}')
        else:
            print(f'O menor número é o {num2}')
    elif opcao == 7:
        num1 = int(input('Digite o primeiro número novamente: '))
        num2 = int(input('Digite o segundo número novamente: '))
    elif opcao == 8:
        print('Finalizando...')
    else:     
        print('\033[1;31mDigite uma opção válida.\033[m')
print('=-=-=FIM DO PROGRAMA=-=-=')