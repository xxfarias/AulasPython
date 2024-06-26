num = int((input('Digite um numero de 0 a 9999: ')))
num1 = str(num+10000)
print("""
No número: {} 
Milhar: {} 000
Centena: {} 00
Dezena: {} 0
Unidade: {}
""".format(num1[1:5], num1[1], num1[2], num1[3], num1[4]))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('milhar: {}, centena {}, dezena {}, unidade {}'.format(m, c, d, u))