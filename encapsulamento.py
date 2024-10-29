class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if "clientes" not in self.dados:
            self.dados["clientes"] = {id: nome}
            print(self.dados)
        else:
            self.dados["clientes"].update({id: nome})
            print(self.dados)


bd = BaseDeDados()

bd.inserir_cliente(2, "Gabriel")
bd.inserir_cliente(3, "Lira")
bd.inserir_cliente(4, "Santos")