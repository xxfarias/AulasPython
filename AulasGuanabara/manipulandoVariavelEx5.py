# frase = str(input('Digite uma frase: ')).strip().upper()
# contador = frase.count("A")
# print('Sua frase tem {} A'.format(contador))
# print('O primeiro A aparece na posição {}'.format(frase.find('A')+1))
# print('O ultimo A aparece na posição {}'.format(frase.rfind('A')+1))


frase = str(input('Digite uma frase: ')).strip().upper()
letra = (input('Digite a letra a ser analisada: ')).strip().upper()
contador = frase.count(letra)
print('Na sua frase "{}" tem a "{}" letra {} vezes'.format(frase, letra, contador))