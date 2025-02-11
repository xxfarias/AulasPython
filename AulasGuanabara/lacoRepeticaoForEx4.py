num = int(input('Digite o número para gerar a tabuada: '))
for c in range (1, 11):
    resultado = num * c
    print(f'{num} * {c} = {resultado}')
print('FIM')