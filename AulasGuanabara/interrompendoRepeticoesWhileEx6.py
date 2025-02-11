# Caixa eletrônico
print('='*50)
print(f'{'CAIXA ELETRÔNICO FARIAS':^50}')
print('='*50)
while True:
     valorSacado = int(input('Quanto você quer sacar? R$'))
     cedulasCem = valorSacado // 100
     valorSacado -= cedulasCem*100
     cedulasCinquenta = valorSacado // 50
     valorSacado -= cedulasCinquenta*50
     cedulasDez = valorSacado // 10
     valorSacado -= cedulasDez * 10
     cedulasCinco = valorSacado // 5
     valorSacado -= cedulasCinco * 5
     cedulasUm = valorSacado // 1
     break
if cedulasCem > 0:
     print(f'\033[1;34m{cedulasCem} cédulas de R$100,00\033[m')  
if cedulasCinquenta > 0:
     print(f'\033[1;33m{cedulasCinquenta} cédulas de R$50,00\033[m')
if cedulasDez > 0:
     print(f'\033[1;36m{cedulasDez} cédulas de R$10,00\033[m')
if cedulasCinco > 0:
     print(f'\033[1;35m{cedulasCinco} cédulas de R$5,00\033[m')
if cedulasUm > 0:
     print(f'\033[1;32m{cedulasUm} cédulas de R$1,00\033[m')
 