palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in palavras:
    print(f'\nA palavra {c} tem as vogais: ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra,end='')