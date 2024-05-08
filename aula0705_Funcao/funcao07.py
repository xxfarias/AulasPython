def calcularMedia(notas):
    total = sum(notas)
    print("Total é: ", total)
    media = total / len(notas)
    print("Divisor: ", len(notas))
    return media

notas = [7.5, 8.0, 6.5, 9.0]
media = calcularMedia(notas)
print("A média é: ", media)