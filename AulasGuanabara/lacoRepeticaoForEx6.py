# Progressao aritimética
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for c in range (primeiroTermo, primeiroTermo + (razao * 10), razao):
    print(c, end=' ')
print('-=-FIM-=-')