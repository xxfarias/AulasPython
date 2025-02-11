# 10 primeiros termos da PA
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 0
limite = 9
somador = 0
while contador <= limite:
    while contador <= limite:
        print(primeiroTermo)
        primeiroTermo = primeiroTermo + razao
        contador = contador + 1
    somador = int(input('Quantos termos a mais: '))
    limite += somador
print(f'Fim com {contador} termos exibidos.')