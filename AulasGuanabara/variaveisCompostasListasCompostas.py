lista = []
lista.append('Guilherme')
lista.append(22)
print(lista)
pessoas = []
pessoas.append(lista[:])
print(pessoas)
lista[0] = 'João'
lista[1] = 34
pessoas.append(lista[:])
print(pessoas)
pessoas[1] = ['Cleiton', 50]
print(pessoas)
print('-='*30)
galera = [['João','19'],['Ana', '33'], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
print('-='*30)
galera = []
dados = []
for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera) 