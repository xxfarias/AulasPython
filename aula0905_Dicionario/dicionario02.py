dicionario = {"gato":"chat", "cachorro":"cien","cavalo":"cheval"}
palavras = ['gato', 'lion', 'cavalo']

for palavra in palavras:
    if palavra in dicionario:
        print(palavra, "->", dicionario[palavra])
    else:
        print(palavra, "não está no dicionário")