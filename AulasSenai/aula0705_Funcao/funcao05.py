def funcaoDetecta(n):
    if(n % 2 == 0):
        return "É par"
    else:
        return "É ímpar"
    
print (funcaoDetecta(int(input("Entre com um número: "))))