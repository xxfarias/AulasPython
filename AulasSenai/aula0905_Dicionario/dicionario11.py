agenda = {}
while True:
    nome = input("Digite o nome da pessoa")
    if nome == '':
        break
    telefone = input("Digite o telefone: ")
    # Adiciona o telefone ao dicionário
    agenda[nome] = telefone
    # Pesquisa um telefone na agenda
nomePesquisa = input("Digite o nome para pesquisar")
if nomePesquisa in agenda:
    print("Telefone de",nomePesquisa,":",agenda[nomePesquisa])
else:
    print("Nome não encontrado na agenda. ")