def fatorial(num, show=False):
    """Calcula o Fatorial de um número
    Args:
        num (int): O número a ser calculado
        show (bool, optional): Mostrar ou não a conta
    Returns:
        O valor do Fatorial de um número n 
    """
    fact = 1
    for c in range(num, 0, -1):
        fact *= c
        if show == True and c > 1:
            print(f'{c} * ',end='')
        if show == True and c == 1:
            print(f'{c} = ',end='')
    return fact
print(fatorial(6))
print('-'*30)
print(fatorial(6, True))
help(fatorial)