votos = {}
while True:
    candidato = input ("Digite o nome do canditado (ou 'fim' para encerrar)")
    if candidato == "fim":
        break
    # Verifica se o canditado já recebeu votos antes
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1
    # Imprime o resultado da votação
print("Resultado da votação:")
for canditado, quantidade in votos.items():
    print(candidato, "-", quantidade, "votos")
print(votos)