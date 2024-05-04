# 1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.
num = int(input("Digite um valor inteiro: "))
contador = 0
if num > 10 or num <0:
    print("INVALIDO")
else:
    while (contador<=10):
        print(num * contador)
        contador +=1


