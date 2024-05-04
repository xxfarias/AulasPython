# removedor de vogais
palavraSemVogal= ""
palavraUsuario = input("Entre com uma palavra: ")
palavraUsuario = palavraUsuario.upper()

for letra in palavraUsuario:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palavraSemVogal += letra
print(palavraSemVogal)