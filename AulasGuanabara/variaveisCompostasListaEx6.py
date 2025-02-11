# lista = []
# lista = str(input('Digite uma expressão: '))
# contadorParentesAberto = lista.count('(')
# contadorParentesFechado = lista.count(')')
# if contadorParentesAberto == contadorParentesFechado:
#     print('A expressão está correta!')
# else:
#     print('A expresão está incorreta!')

# Solução 2 com pilha
pilha = []
expressao = str(input('Digite a expressão: '))
for c in expressao:
    if c in "(":
        pilha.append('(')
    elif c in ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print(f'\033[32;1mSua expressão está correta!\033[m')
else:
    print(f'\033[31;1mSua expressão está incorreta!\033[m')
# Essa solução evita validar expressões como: )a+b(    
