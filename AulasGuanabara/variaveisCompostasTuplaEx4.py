valores = (int(input('Digite o primeiro valor: ')), 
           int(input('Digite o segundo valor: ')), 
           int(input('Digite o terceiro valor: ')), 
           int(input('Digite o quarto valor: ')))
print(f'Os valores digitados foram: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na {valores.index(3)+1}ª posição')
else:
    print('Não foi digitado valor 3')
print('Os valores pares digitados foram: ',end='')
for c in valores:
    if c % 2 == 0:
        print(c,end='')