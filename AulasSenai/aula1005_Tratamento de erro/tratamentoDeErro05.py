while True:
    try:
        numero = int(input("Entre com um número int: "))
        print(5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou não é possivel dividir por zero.")
    except:
        print("Desculpe, algo errado aconteceu")