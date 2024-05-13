# para __init__ o primeiro item é usado como referência
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def escreveNome(abc):
        print("Olá meu nome é: "+ abc.nome)
nome1 = Pessoa("Emengarda", 44)
nome1.escreveNome()
# Modificar o objeto
nome1.idade = 23
print(nome1.idade)
nome1.nome = "Guilherminda"
print(nome1.nome)