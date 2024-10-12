"""
class Teste:
    def __init__(self, valor):
        self.x = valor
    # Metodo Getter
    def gat_valor(self):
        return self.x

    # Metodo Setter
    def set_valor(self, valor):
        self.x = valor

teste = Teste(10)
print("O valor do get é: ", teste.gat_valor())

teste.gat_valor(50)
print(teste.gat_valor()


"""
# Outro exenplo
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco * (porcentagem / 100))

    #Getter
    def preco(self):
        return self._preco

    #Setter
    def preco(self, valor):
        if isinstance(self.preco, str):
            self.valor = float(preco.replace("RS", ""))
        self.preco = valor



p1 = Produto("notebook", 1000)
p1.desconto(10)
p1.desconto(10)
print(p1.preco)











