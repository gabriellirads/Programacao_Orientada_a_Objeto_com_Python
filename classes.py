# Gabril
class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.n = nome
        self.i = idade
        self.c = comendo
        self.f = falando

    def comer(self, alimento):
        self.alimento = alimento
        if self.c: #
            print(f"{self.n} já está comendo!")
            return

        print(f'{self.n} está comendo {self.alimento}')
        self.c = True

    def parar_comer(self):
        if not self.c:
            print(f'{self.n} não etá comendo!')
            return

        print(f'{self.n} parou de comer!')
        self.c = False

    def falar(self, assunto):
        self.assunto = assunto
        if self.c:
            print(f'{self.n} não pode falr comendo!')
            return

        if self.f:
            print(f'{self.n} já está falando!')
            return

        print(f'{self.n} está falando sobre {self.assunto}')



# Instanciado a clases!
pessoa1 = Pessoa("Maria", 26)
print(f'Nome: {pessoa1.n} Idade: {pessoa1.i}')
pessoa2 = Pessoa("Pedro", 30)
print(f"Nome: {pessoa2.n} Idade: {pessoa2.i}")

pessoa1.comer("maçã")# O objeto pessoa1 irar começar a comer!
pessoa1.comer('banana')# O obeto não irar começar comer, pois já esta comendo!

pessoa1.parar_comer()
pessoa1.parar_comer()

pessoa1.falar("politica")# O objeto pessoa1 ira começar falar, pois nao está comendo nem já estava falando!
pessoa1.comer("uva")# O objeto pessoa1 ira começar a comer!
pessoa1.falar("Programaçãp")# O objeto pesssoa1 não irar falar pois está comendo!