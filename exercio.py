class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque


    def veder(self, quantidade):
        if self.estoque > 0:
            self.quantidade = quantidade
            self.estoque -= self.quantidade
        else:
            print("Livro está indisponivel!")

    def repor(self, quantidade):
        if self.quantidade > 0:
            self.estoque += self.estoque
        else:
            print("Auantidade invalida!")


    def mostra_detalhes(self):
        print(f" Titulo: {self.titulo} \n Autor: {self.autor} \n Preço: {self.preco} \n Estoque: {self.estoque}")

titulo = str(input("Titulo: "))
autor = str(input("Autor: "))
preco = float(input("Preço: "))
estoque = int(input("Estoque: "))

p1 = Livro(titulo, autor, preco, estoque)
p1.mostra_detalhes()

p1.veder(1)
p1.mostra_detalhes()
p1.veder(1)
p1.repor(10)
p1.mostra_detalhes()

