from random import randint
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade, ):
        self.nome = nome
        self.idade = idade


    def gat_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nasc(cls, nome, ano_nascimento):
        i = cls.ano_atual - ano_nascimento
        return cls(nome, i)

    @staticmethod
    def criar_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa.por_ano_nasc("Luiz" , 1998)
print(p1.nome, p1.idade)
p1.gat_ano_nascimento()

print(Pessoa.criar_id())#Usando o metodo estatico pela classes "Pessoa"
print(p1.criar_id())#Usando o metodo estatico pela estancia "p1"
