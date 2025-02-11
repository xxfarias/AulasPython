precoProdutoBarato = contador = produtosMil = totalGasto = 0
nomeProdutoBarato = ''
while True:
    escolha = ''
    nome = str(input('Nome: ')).strip()
    preco = float(input('Preço: R$'))
    if preco > 1000.00:
        produtosMil += 1
    if contador == 0 or preco < precoProdutoBarato:
        precoProdutoBarato = preco
        nomeProdutoBarato = nome
    totalGasto += preco
    contador += 1
    print('\033[1;32mProduto cadastrado!\033[m')
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()
    if escolha == 'N':
        break
    print('='*50)
print('='*50)
print(f'O total gasto foi de R${totalGasto:.2f}\n{produtosMil} produtos custam mais de R$1000,00\nO produto mais barato é o {nomeProdutoBarato} custando R${precoProdutoBarato:.2f}')