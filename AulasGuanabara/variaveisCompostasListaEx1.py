listaA = []
for c in range(0,5):
    listaA.append(int(input(f'Digite o valor {c+1}: ')))
print(f'Lista A: {listaA}')
print(f'O maior valor digitado foi {max(listaA)} e se encontra na posição {listaA.index(max(listaA))+1}')
print(f'O menor valor digitado foi {min(listaA)} e se encontra na posição {listaA.index(min(listaA))+1}')