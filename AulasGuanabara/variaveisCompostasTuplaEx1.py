from time import sleep
numeros = ('Zero','Um', 'Dois','Três','Quatro', 'Cinco', 'Seis', 
           'Sete', 'Oito', 'Nove', 'Dez', 'Onde','Doze','Treze',
           'Quatrorze','Quinze','Dezesseis','Dezessete','Dezoito',
           'Dezenove','Vinte')
while True:
    while True:
        contador = int(input('Digite um número (Entre 0 e 20): '))
        if 0<=contador <=20:
            break
        print('\033[1;31mINVÁLIDO. Digite um número entre 0 e 20.\033[m')
    print(numeros[contador])
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('\033[32;1mQuer continuar? [S/N]\033[m')).strip().upper()[0]
    if continuar == 'N':
        break
    sleep(0.1)
    print('-'*50)
sleep(0.2)
print('Programa finalizado')