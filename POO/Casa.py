class Casa:
    def __init__(self, cor, quartos, addquartos): #construtor
        self.cor = cor
        self.quartos = quartos
        self.addquartos = addquartos
        
    def mostrar_cor(self):
        print(f'\ncasa é {self.cor}!!!!')

    def mostrar_quartos(self):
        print(f'\nEsta casa tem {self.quartos} quartos')

    def adicionar_quartos(self):
        addq = self.addquartos + self.quartos
        print(f'\nesta casa tem {addq} quartos depois de ter sido adicionado {self.addquartos}')

    def pintar_casa(self, nova_cor):
        
        print(f'\ncor anterior {self.cor}, agora a nova está sendo {nova_cor}')
        mudanca = self.cor = nova_cor

# passando os valores através dos parametros
casa1 = Casa('Azul', 5, 5)
casa2 = Casa('Purple', 6, 5)

print("===" * 10 + "\ncasa1")
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.adicionar_quartos()
casa1.pintar_casa('vermelho')

''' 
print("===" * 10 + "\ncasa2")
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.adicionar_quartos()
#mostrar_cor(self)
'''