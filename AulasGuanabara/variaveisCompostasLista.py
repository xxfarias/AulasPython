lista = [2, 5, 9, 1]
print(lista)
# mudando o primeiro valor
lista[0] = 3
# Adicionando o '4'
lista.append(4)
# Adicionando o 99 na primeira posição
lista.insert(0, 99)
print(lista)
print(f'A lista possui {len(lista)} elementos.')
# Removendo o valor '9' pelo indice
print('Removendo o 9: ',end='')
lista.pop(3)
print(lista)
# removendo o 99 pelo nome
print('Removendo o 99: ',end='')
if 99 in lista:
    lista.remove(99)
else:
    print('O 99 não foi encontrado')
print(lista)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c in valores:
    print(f'{c} ',end='')
print()
print('-'*20)
for c in range (0, len(valores)):
    print(f'Na posição {c}, o valor é {valores[c]}')
print('-'*20)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('-'*50)
# Criando uma lista e adicionando valores
listaFor = []
for c in range(0,5):
    listaFor.append(int(input(f'Digite o valor {c} para a lista: ')))
print(listaFor)
print('-'*50)
# Conetando listas:
print('Copiando e conectando listas: ')
listaA = [2, 3, 4, 7]
print(listaA)
listaB = listaA
# Modificando a lista B
listaB[2] = 99
# Observe que a lista A também foi modificada
print(f'Lista A:{listaA}, lista B: {listaB}')
# Copiando listas:
listaC = listaB[:]
listaC.append(1005)
print('A lista C é uma cópia da lista B, posso modifica-la sem alterar a lista B.')
print(f'Lista B: {listaB}, lista C: {listaC}')