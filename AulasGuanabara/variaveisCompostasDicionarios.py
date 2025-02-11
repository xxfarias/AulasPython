# {dicionários}
pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade' ])
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
print('-'*30)
for key in pessoas.keys():
    print(key)
print('-'*30)
for value in pessoas.values():
    print(value)
print('-'*30)
pessoas['peso'] = 79.5
pessoas['nome'] = 'Guilherme'
for key, value in pessoas.items():
    print(f'{key} = {value} ')
print('-'*30)
# Dicionário dentro da lista
print('Dicionário dentro da lista')
brasil = list()
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
print('-'*30)
estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Digite a UF: '))
    estado['sigla'] = str(input('Digite a Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor = {v}',end='')
    print()