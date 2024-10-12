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



p1 = Pessoa.por_ano_nasc("Luiz" , 1998)
print(p1.nome, p1.idade)
p1.gat_ano_nascimento()

