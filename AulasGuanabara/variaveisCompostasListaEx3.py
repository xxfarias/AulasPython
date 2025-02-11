lista = []
for c in range(0,5):
    num = int(input(f'Digite o valor {c+1}: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Valor maior adicionado: {lista}')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos}: {lista}')
                break
            pos += 1
print(lista)