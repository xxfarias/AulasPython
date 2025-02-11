def leiaInt(num):
    while True:
        valor = input(num)
        if valor.isnumeric():
            return valor
        else:
            print('\033[31;1mErro! Digite um número inteiro.\033[m')
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')