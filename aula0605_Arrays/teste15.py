minhaLista = [17, 8, 10, 6, 2, 4] # lista para ordenar
trocado = True # Precisamos dele para entrar no loop while

while trocado:
    trocado = False # Sem trocas até agora
    for i in range(len(minhaLista) - 1):
        if minhaLista[i] > minhaLista[i + 1]:
            trocado = True # Ocorreu uma troca!
            minhaLista[i], minhaLista[i + 1] = minhaLista[i + 1], minhaLista[i]

print(minhaLista)