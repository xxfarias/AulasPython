# para __init__ o primeiro item é usado como referência
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def escreve(self):
        print(self.nome, self.idade)
class Estudante(Pessoa):
    def __init__(self, nome, idade, ano):
        super().__init__(nome, idade)
        self.graducao = ano
    def bemVindo(self):
        print("Bem-vindo", self.nome, "para a classe", self.graducao)
x = Estudante("Jo", 21, 2024)
x.bemVindo()