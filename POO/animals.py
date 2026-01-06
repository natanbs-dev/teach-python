class Animal: #classe pai
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie


    def apresentar(self):
        print('***' * 20)
        print(f'\nNOME={self.nome} \nCOR={self.cor}, \nESPECIE={self.especie}')


class Gato(Animal): #classes filhas, que herdam todos os métodos [apresentar]
    def emitir_som(self):
        print('miau')

class Cachorro(Animal):
    def emitir_som(self):
        print('au au')

class Elefante(Animal):
    def emitir_som(self):
        print('pruuuu')

gato1 = Gato('felix', 'white', "siames")
gato1.apresentar()
gato1.emitir_som()

cachorro1 = Cachorro('spike', 'preta', 'vira-lata')
cachorro1.apresentar()
cachorro1.emitir_som()

elefante1 = Elefante('tux', 'gray', 'many')
elefante1.apresentar()
elefante1.emitir_som()