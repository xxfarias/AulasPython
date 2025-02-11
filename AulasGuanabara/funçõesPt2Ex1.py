def voto(anoNasc):
    from datetime import datetime
    idade = datetime.now().year - anoNasc
    if 65 > idade >= 18:
        return f'Com {idade} anos, seu voto é OBRIGATÓRIO'
    elif 18 > idade >= 16 or idade >= 65:
        return f'Com {idade} anos, seu voto é OPCIONAL'
    else:
        return f'Com {idade} anos, seu voto é NEGADO'
anoNascimento = int(input('Digite o seu ano de nascimento: '))
print(f'{voto(anoNascimento)}')
