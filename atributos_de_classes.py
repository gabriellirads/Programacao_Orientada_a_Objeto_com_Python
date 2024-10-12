class A:
    vc = 123
    nome = "Gabriel Lira"

a1 = A()
a2 = A()
print(a1.vc)
print(a2.vc)
print(A.vc) # Imprime a variavel da classe sem instanciar!
A.nome = "Lira Gabriel" # Altera o valor da variavel da clases!
print(A.nome)# Imprimir o valor da variavel da classe sem instanciar!