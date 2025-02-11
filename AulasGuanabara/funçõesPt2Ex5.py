def notas(*n, sit=False):
    """Função para retornar quantidade de notas, maior nota, menor nota, média e situação
        Parametros: 
        *n = Uma ou mais notas dos alunos
        sit(False) = valor opicional, mostra a situação da turma
        return: dicionário com várias informalções da turma
    """
    resultado = dict()
    somador = maiorNota =menorNota= contador = 0
    for c in n:
        contador += 1
        somador += c
        if contador == 1:
            maiorNota = c
            menorNota = c
        if c < menorNota:
            menorNota = c
        if c > maiorNota:
            maiorNota = c
    resultado['quantidadeNotas'] = contador
    resultado['maiorNota'] = maiorNota
    resultado['menorNota'] = menorNota
    media = somador / contador
    resultado['media'] = media
    if sit == True:
        if media >= 7:
            resultado['situação'] = 'APROVADO'
        elif 7 > media >= 5:
            resultado['situação'] = 'RECUPERAÇÃO'
        else:
            resultado['situação'] = 'REPROVADO'
    return resultado
print(notas(9, 6, 2, 4, sit=True))
print(notas(10, 6, 8, 7, sit=True))
print(notas(5, 3, 3, 2, 1, sit=True))