# Dissecando uma váriavel
num1 = input('Digite algo: ')
print('O tipo digitado é {}'.format(type(num1)))
print('Ele é númerico? {}'.format(num1.isnumeric()))
print('Ele é alfabético? {}'.format(num1.isalpha()))
print('Ele é alfanúmerico? {}'.format(num1.isalnum()))
print('Ele tem todas as letras MAISCULAS? {}'.format(num1.isupper()))
print('Ele tem todas as letras minusculas? {}'.format(num1.islower()))
print('Ele é capitalizado? {}'.format(num1.istitle()))
print('Ele é um espaço vazio? {}'.format(num1.isspace()))
print('---------------\nFim do código')
# '\n' quebra a linha do código
