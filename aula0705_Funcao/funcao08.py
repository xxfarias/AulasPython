def calcularFatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcularFatorial(numero-1)
    
numero = 5
fatorial = calcularFatorial(numero)
print("O faltoral de",numero,"é",fatorial)