cores = {'limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m', 'roxo':'\033[35m', 'ciano':'\033[36m', 'cinza':'\033[37m', 'pretoebranco':'\033[7;30m'}
preco = float(input('Digite o preço do produto: '))
pagamento = int(input('Digite a forma de pagamento: \n1 - À vista dinheiro/cheque - 10% de desconto \n2 - À vista no cartão - 5% de desconto \n3 - Em até 2x no cartão - Preço normal \n4 - 3x ou mais no cartão - 20% de juros\n'))
if pagamento ==1:
    novoPreco = preco - (preco * 0.1)
    print(f'O preço final será de {cores["roxo"]}R${novoPreco:.2f}{cores["limpa"]}')
elif pagamento == 2:
    novoPreco = preco - (preco * 0.05)
    print(f'O preço final será de {cores["verde"]}R${novoPreco:.2f}{cores["limpa"]}')
elif pagamento == 3:
    parcela = preco /2
    print(f'A sua compra será parcelada em 2* de R${parcela:.2f}.')
    print(f'O preço final será de {cores["azul"]}R${preco:.2f}{cores["limpa"]}')
elif pagamento == 4:
    parcela = int(input('Em quantas parcelas? '))
    precofinal = preco + (preco*0.2)
    parcelaMensal = precofinal / parcela
    print(f'A sua compra será parcelada em {parcela}* de R${parcelaMensal:.2f}')
    print(f'O preço final será de {cores["pretoebranco"]}R${precofinal:.2f}{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}Forma de pagamento inválida.{cores["limpa"]}')