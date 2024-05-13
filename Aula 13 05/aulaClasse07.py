# para __init__ o primeiro item é usado como referência
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def escreve(self):
        print(self.nome, self.idade)
class Estudante(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.graducao = 2024
x = Estudante("Jo", 21)
x.escreve()
print(x.graducao)