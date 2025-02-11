from time import sleep

# Maior
def maior(*num):
    lista = list()
    lista.append(num)
    for c in lista:
        print(f'Analisando a lista {c}...')
        sleep(1)
        print(f'Foram informados {len(c)} valores e o maior valor é o {max(c)} e o menor é o {min(c)}')

maior(10, 50, 20)
maior(60, 100, 12, 321, 32, 132, 67, 407)

lista = list()
while True:
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

maior(*lista)