print('\033[4;33;41mOlá, Mundo!\033[m')
print('A aula de cores foi \033[35mboa\033[m!!!')
nome = 'Guilherme'
print('Olá, \033[1;32m{}\033[m. Como você está?'.format(nome))
print('Seja bem vindo ao teste de cores, {}{}{}. Este é o começo!'.format('\033[1;31m', nome, '\033[m'))
cores = {'preto':'\033[7;30m', 
         'vermelho':'\033[1;31m',
         'limpa':'\033[m'}
print('Essa é a cor {}preta{}!'.format(cores['preto'], cores['limpa']))
print('Essa é a cor {}vermelha{}!'.format(cores['vermelho'], cores['limpa']))
