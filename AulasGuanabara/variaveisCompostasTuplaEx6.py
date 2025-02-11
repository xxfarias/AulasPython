palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')
for cont in range (0,len(palavras)):
    print(f'\nNa palavra {palavras[cont].upper()} temos as vogais:',end='')
    for letra in palavras[cont]:
        if letra.lower() in 'aeiou':
            print(letra,end='')