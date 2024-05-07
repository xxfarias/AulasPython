minhaLista = []
trocado = True
num = int(input("Quantos elementos deseja? "))
for i in range(num):
    val = float(input("Entre com o número: "))
    minhaLista.append(val)
while trocado:
    trocado = False
    for i in range(len(minhaLista)-1):
        if minhaLista[i] > minhaLista[i + 1]:
            trocado = True
            minhaLista[i], minhaLista[i + 1] = minhaLista[i + 1], minhaLista[i]

print("\nOrdenado:")
print(minhaLista)