frase = 'Três pratos de trigo para três trigres tristes'
print(frase[31:39])
print(frase[::4])
print('O tamanho da frase "{}" é de: {} espaços'.format(frase, len(frase)))
print(frase.count('i')) #Conta quantos "i" tem na frase
print('A frase "{}" tem o total de {} "s"'.format(frase, frase.count('s')))
print(frase.find('ri')) #Essa função mostra a posição
print('Existe a palavra "Três" na frase {}: {}'.format(frase, "Três" in frase)) #Usando o IN
print(frase.replace('trigres', 'trigos'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
fraseDividida = frase.split() #Cria uma lista a partir da string, dividindo
print(fraseDividida)
print('-'.join(fraseDividida))
frase2 = '  João  '
print(frase2.strip()) #Essa função tira os espaços inuteis
print(frase2.rstrip()) #Essa função remove os espaços da direita, pelo R de right
print(frase.upper().count('RI')) #Unindo funções