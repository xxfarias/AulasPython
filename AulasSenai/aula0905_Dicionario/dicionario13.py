produtos = {
    'banana':2.50,
    'maça':3.00,
    'laranja':2.75,
    'abacaxi': 4.50,
    'manga': 3.50
}
# Imprimir o preço de uma maça
print('O preço de uma maça é: R$'+ str(produtos['maça']))
# Adicionar um novo produto
produtos['melancia'] = 6.00
# Imprimir todos os produtos e seus preços
for produto, preco in produtos.items():
    print(produto + ': R$' + str(preco))
print(produtos)