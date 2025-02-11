# Palíndromo
frase = str(input('Digite uma frase:\n')).strip().upper().replace(" ",'')
fraseInversa = frase[::-1]
print(f'A frase inversa é "{fraseInversa}"')
if frase == fraseInversa:
    print('A frase é um palíndromo!')
elif frase != fraseInversa:
    print('A frase não é um palíndromo!')
else:
    print('Digite uma frase válida. ')