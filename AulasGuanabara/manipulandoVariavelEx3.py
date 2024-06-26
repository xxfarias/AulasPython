# nomeCidade = input('Digite o nome da sua cidade: ')
# nomeCidadeDividido = nomeCidade.split()
# if nomeCidadeDividido[0] == 'São' or nomeCidadeDividido[0] == 'Sao':
#     print('Sua cidade começa com São')
# else:
#     print('Sua cidade não começa com São')
    
nomeCidade = input('Digite o nome da sua cidade: ')
nomeCidade = nomeCidade.upper()
nomeCidade = nomeCidade.strip()
nomeCidade = nomeCidade.split()
print('Sua cidade começa com "Santo"? {}, sua cidade é {}'.format("SANTO" in nomeCidade[0], nomeCidade))

