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
x = Estudante("Jo", 21)
x.escreve()