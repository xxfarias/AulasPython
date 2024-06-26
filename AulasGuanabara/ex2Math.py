import math
catetoOposto = int(input('Entre com o cateto oposto: '))
catetoAdjascente = int(input('Entre com o cateto adjascente: '))
hipotenusa = math.hypot(catetoAdjascente, catetoOposto)
print(hipotenusa)