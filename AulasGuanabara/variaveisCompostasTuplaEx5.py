itensPrecos = ('Lápis',1.75,
               'Borracha',2.00,
               'Caderno',15.90,
               'Estojo',25,
               'Transferidor',4.20,
               'Compasso',9.99,
               'Mochila',120.32,
               'Caneteas',22.30,
               'Livro',34.90)
print('-'*50)
print(f'{'LISTA DE PREÇOS':^50}')
print('-'*50)
for pos in range(0, len(itensPrecos)):
    if pos % 2 == 0:
        print(f'{itensPrecos[pos]:.<40}', end='')
    else:
        print(f'R${itensPrecos[pos]:>7 .2f}')
print('-'*50)