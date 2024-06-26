# 0 - Peça para  o usuário entrar com dois valores (primeiro e último).
# Faça a contagem entre esses números.
# Caso o último for menor que  o primeiro faça a contagem decrescente.
# Caso o último número for maior que o primeiro faça a contagem crescente.


primeiro = int(input("Digite o primeiro valor: "))
ultimo = int(input("Digite o último valor: "))

# Verifica se o último é menor que o primeiro
if ultimo < primeiro:
    # Contagem decrescente
    while primeiro >= ultimo:
        print(primeiro)
        primeiro -= 1
else:
    # Contagem crescente
    while primeiro <= ultimo:
        print(primeiro)
        primeiro += 1

