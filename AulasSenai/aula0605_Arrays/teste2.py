# Criando uma lista
minhaLista = [1, 2, 3, 4, 5]
# Usando um loop for para percorrer a lista e imprimir cada elemento
for i in range(len(minhaLista)):
    print("O elemento", i+1, "da lista é: ", minhaLista[i])

# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Usando um loop for para percorrer a lsita e imprimir cada elemento
for numero in numeros:
    print(numero, " - Com for")
    
# Usando um loop while para percorrer a lista e imprimir cada elemento
i = 0
while i < len (numeros):
    print(numeros[i], " - Com While")
    i += 1