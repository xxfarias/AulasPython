# para __init__ o primeiro item é usado como referência
class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age
nome1 = Pessoa("Joaquina", 99)
print(nome1.name)
print(nome1.age)