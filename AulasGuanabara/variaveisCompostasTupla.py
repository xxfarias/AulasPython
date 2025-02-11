lista = ('arroz', 'feijao')
lista = ('suco', 'bolacha')
print(lista)
lanche = ('hamburguer','suco','pizza','pudim')
for comida in lanche:
    print(f'Comendo {comida}')
print('='*30)
# O caso abaixo é útil quando for necessário mostrar a posição do contador
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('='*30)
for posicao, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posicação {posicao}')
print('='*50)
print(sorted(lanche))
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(sorted(c))
print(len(lanche))
print(c.count(2))
# Conta quantos 2 tem na tupla
print(c.index(2))
# Busca a posição na tupla
