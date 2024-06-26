cadastro = {}
while True:
    nome = input("Digite o nome completo: ")
    if nome == '':
        break

    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")

    # Adiciona os dados ao dicionário
    cadastro[nome] = {"idade":idade, "cidade":cidade}

# Imprime o cadastro completo
print("Cadastro:")
print(cadastro)
for nome, dados in cadastro.items():
    print("- Nome:", nome)
    print(" Idade:", dados["idade"])
    print(" Cidade:", dados["cidade"])