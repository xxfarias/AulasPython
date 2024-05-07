# Criando uma lista com elementos duplicados
listaComDuplicatas = [1, 2, 3, 1, 4, 2, 5, 6, 3, 7, 8, 5, 9]
# Inicializando uma lista vazia pura
# Armazenar os elementos únicos
listaSemDuplicatas = []
# Usando um loop while para percorrer
# A lista e remover os elementos duplicados

print("A lista com duplicatas é:", listaComDuplicatas)

while listaComDuplicatas:
    elemento = listaComDuplicatas.pop(0)
    # pop é usada para remover o elemento
    if elemento not in listaSemDuplicatas:
        listaSemDuplicatas.append(elemento)

# Imprimindo o resultado
print("A lista com duplicatas é:", listaComDuplicatas)
print("A lista sem duplicatas é:", listaSemDuplicatas)