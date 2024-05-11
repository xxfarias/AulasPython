while True:
    try:
        numero = int(input("Entre com um número: "))
        print(numero/2)
        break
    except:
        print("O número que você entrou não é válido. Tente novamente")
    