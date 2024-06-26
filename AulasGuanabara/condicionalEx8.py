ladoA = int(input('Digite o comprimento do primeiro lado: '))
ladoB = int(input('Digite o comprimento do segundo lado: '))
ladoC = int(input('Digite o comprimento do terceiro lado: '))
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print('\033[1;32mÉ um triângulo!\033[m')
else:
    print('\033[1;31mNão é um triângulo\033[m')