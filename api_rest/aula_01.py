# variaveis
from operator import truediv

texto = "hello world"
numerico = 10
list = ['i1', 'i2']
dict = {"chave":"valor", "chave2":"valor2"}
boleanos = True

if False:
    print (texto)
    print (numerico)
    print (dict)
    print (list[1])
    print (boleanos)
print("just a comment way")

#metodos

""" 
if False:
    print("This is a comment")
    print("This is another comment")
print("This is not a comment")
"""

print(numerico + 10) #20

def soma(a, b):
    return a + b

print(soma(numerico, 1))
print(soma(numerico, 2))

##clasess

class Mamifero:
    def andar(self):
        print("andar")

# juntando a classe com a classe pai
class Humano(Mamifero):
    def falar(self):
        print("falar")

# juntando a classe com a classe pai2
class Gato(Mamifero):
    def miar(self):
        print("miar")


mamifero = Mamifero()
mamifero.andar()

carlos = Humano()
carlos.andar()
carlos.falar()

banguela = Gato()
banguela.miar()
banguela.andar()