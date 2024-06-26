velocidadeCarro = int(input('Digite a velocidade do carro: '))
if velocidadeCarro > 80:
    excedente = (velocidadeCarro - 80)
    precoMulta = (excedente * 7)
    print('Você ultrapassou o limite de 80km/h')
    print(f'Sua multa vai ser de R${precoMulta},00')
else:
    print('Você não ultrapassou o limite de 80km/h')
print('---FIM---')
