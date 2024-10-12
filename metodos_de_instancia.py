class Produto:
    def __init__(self, nome, preco, categoria):
        self.n = nome
        self.p = preco
        self.c = categoria

    def desconto(self, percentagem):
        self.percentagem = percentagem
        self.p = self.p - (self.p * (self.percentagem / 100))


n = str(input("Qual o nome do produto?: "))
p = float(input("Qual o valor do produto?: "))
c = str(input("Qual a categoria do produto?: "))

p1 = Produto(n, p, c)
print(p1.n, p1.p, p1.c)
des = float(input("Qual a percentagem do desconto?: "))
p1.desconto(des)
print(p1.n, p1.p, p1.c)

