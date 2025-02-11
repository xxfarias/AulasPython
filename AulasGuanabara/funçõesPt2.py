# Interactive help usando o help()
# Tutorial de determinada função
#                   help(print)
# docstrings | String de documentação
def contador(i, f, p):
    """_summary_
    Faz uma contagem e mostra na tela
    Args:
        i: inicio da contagem
        f: fim da contagem
        p: passo da contagem
        return: sem retorno
    """
    c = i
    while c <=f:
        print(f'{c} ', end='')
        c += c
    print('Fim!')
# help(contador)

# Argumentações opcionais | 
# Onde o parametro C já foi definido caso não seja passado
def somar(a = 0, b = 0, c=0):
    s= a + b + c
    print(f'A soma vale {s}')
somar(3, 4)
print('-'*30)
# Escopo local
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')
# Escopo global 
n1 = 2
funcao()
print(f'N1 fora vale {n1}')
print('-'*30)
# Retorno de variaveis
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus calculos deram {r1}, {r2} e {r3}')
print('-'*30)
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print('-'*30)
def par(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False
numero = int(input('Digite um número: '))
print(f'É par? {par(numero)}')